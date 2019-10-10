/*
This class provides access to the network connection and data.
This is a wrapper around the Ip-Helper-Api-DLL (Iphlpapi.dll).
Nearly every functionality is based on the MIB_IFROW2  Struct.

__________________________________________________________________________________________
 
  STRUCTURE MIB_IFROW2 ( MSDN https://docs.microsoft.com/de-de/windows/win32/api/netioapi/ns-netioapi-mib_if_row2?redirectedfrom=MSDN)
| Offset 	| Size 	| Type   	| Description             		    	| Notes          	
|--------	|------	|--------	|-----------------------------	|----------------	
| 0      		| 8    	| INT64  	| InterfaceLuid               			|                	
| 8   		   	| 4    	| UINT   	| InterfaceIndex          		    	|                	
| 12   	  	| 16   	| GUID   	| InterfaceGuid          		     	|                	
| 28   	  	| 514  	| WSTR   	| Alias                       				|                	
| 542    	| 514  	| WSTR   	| Description                		 	|                	
| 1056   	| 4    	| UINT   	| PhysicalAddressLength       	|                	
| 1060   	| 32   	| BYTE   	| PhysicalAddress             		|                	
| 1092   	| 32   	| BYTE   	| PermanentPhysicalAddress   |                	
| 1124   	| 4    	| UINT   	| Mtu                         				|                	
| 1128   	| 4    	| UINT   	| Type ( IFTYPE )           		  	|                	
| 1132   	| 4    	| UINT   	| TunnelType                  			|                	
| 1136   	| 4    	| UINT   	| MediaType                   			|                	
| 1140   	| 4    	| UINT   	| PhysicalMediumType          	|                	
| 1144   	| 4    	| UINT   	| AccessType                  			|                	
| 1148   	| 4    	| UINT   	| DirectionType              		 	|                	
| 1152   	| 4    	| UINT   	| Flags									 	|                	
| 1156   	| 4    	| UINT   	| OperStatus                  			|                	
| 1160   	| 4    	| UINT   	| AdminStatus               		  	|                	
| 1164   	| 4    	| UINT   	| MediaConnectState           	|                	
| 1168   	| 16   	| GUID   	| NetworkGuid                 		|                	
| 1184   	| 4    	| UINT   	| ConnectionType             	 	|                	
| 1188   	| 4    	| XXX    	| XXX                        			 	|                	
| 1192   	| 8    	| UINT64 	| TransmitLinkSpeed       	    	|                	
| 1200   	| 8    	| UINT64 	| ReceiveLinkSpeed           	 	|                	
| 1208   	| 8    	| UINT64 	| InOctets                 			   	|                	
| 1216   	| 8    	| UINT64 	| InUcastPkts                 			|                		
| 1224   	| 8    	| UINT64 	| InNUcastPkts               		 	|                			
| 1232   	| 8    	| UINT64 	| InDiscards                  			|               		 	
| 1240   	| 8    	| UINT64 	| InErrors                   			 	|                			
| 1248   	| 8    	| UINT64 	| InUnknownProtos             		|                			
| 1256   	| 8    	| UINT64 	| InUcastOctets               			| Received bytes 	
| 1264   	| 8    	| UINT64 	| InMulticastOctets           		|                	
| 1272   	| 8    	| UINT64 	| InBroadcastOctets           		|                	
| 1280   	| 8    	| UINT64 	| OutOctets                   			|                	
| 1288   	| 8    	| UINT64 	| OutUcastPkts              		  	|                	
| 1296   	| 8    	| UINT64 	| OutNUcastPkts               		|                	
| 1304   	| 8    	| UINT64 	| OutDiscards                 			|
| 1312   	| 8    	| UINT64 	| OutErrors                   			|                	
| 1320   	| 8    	| UINT64 	| OutUcastOctets              		| Sent Bytes
| 1328   	| 8    	| UINT64 	| OutMulticastOctets          		|                	
| 1336   	| 8    	| UINT64 	| OutBroadcastOctets          	|                	
| 1344   	| 8    	| UINT64 	| OutQLen                     			|                	
  ----------------------------------------------------------------------------------------
   TOTAL:  1352 bytes 

*/
class NetworkAnalyzer ; Author: Leon Morten Richter
{
	
	/*
	Create a new instance of NetworkAnalyzer.
	
	This Class can either be instantiated with interfaceName set to null or to zero or with an interface name.
	If a interface name is provided the class will select the matching interface id.
	
	Examples:
	new NetWorkAnalyzer("Realtek PCIe GbE Family Controller")
	new NetWorkAnalyzer()
	
	*/
	__New(interfaceName:=False)
	{
		; Load library for better performance
		this.lib := DllCall( "LoadLibrary", "Str","Iphlpapi.dll", "Ptr" )
		if (!this.lib)
		{
			MsgBox, 48, Warning, Could not load Iphlpapi.dll. , 3
		}
		; Create MIB Struct and set all values to zero
		this.mib_addr:= this.CreateMIB_IFROW2()
		
		; Set the interface, either by name for by best match
		this.interfaceId:= (interfaceName) ? this.GetInterfaceByName(interfaceName) :  this.GetBestInterface()

		if (this.interfaceId<1)
		{
			MsgBox, 48, Warning, Could not bind to interface. , 3
		}
		; Set refresh timestamp to 0
		this.timestamp := 0
		
		; Call GetNetworkStatus once on instantiation to prevent garbage values on first call
		this.GetNetworkStatus(Rx, Tx, RxBPS, TxBPS)
	}
	
	/*
	Delete the instance and unload the library.
	*/
	__Delete()
	{
		DllCall( "FreeLibrary", "Ptr",this.lib ) 
	}
	
	/*
	Used to get properties which are NOT KNOWN by the script
	*/
	__Get(name)
	{
		if(name == "interfaceId")
		{
			Return NumGet( this.mib_addr+  8,   "UInt" )
		}
	}
	
	/*
	Used to set properties which are NOT KNOWN by the script
	*/
	__Set(name, val)
	{
		if(name == "interfaceId")
		{
			this.SetToZero(this.mib_addr,12)
            NumPut( val, this.mib_addr+8, "UInt" )
		}
	}
	
	/*
	Performs a call to the GetIfEntry2 DLL.
	!!! This method requires Windows Vista or higher !!!
	Stores multiple values by reference.
	ExitCode is 0 on success and != 0 on error.
	*/
	GetNetworkStatus(ByRef Rx, ByRef Tx, ByRef RxBPS, ByRef TxBPS)
	{
		Local OldRx, OldTx, OldTimestamp
		; backup old RX / TX values for comparism
		OldRx := NumGet( this.mib_addr+1256, "Int64" )
		OldTx := NumGet( this.mib_addr+1320, "Int64" )
		
		;Call DLL and store the result inside our MIB struct
		ErrorLevel:= DllCall( "iphlpapi\GetIfEntry2", "Ptr", this.mib_addr)
		if (ErrorLevel)
		{
			this.SetToZero(this.mib_addr)
			return -1
		} 
		
		Rx := NumGet( this.mib_addr+1256, "Int64" )
		Tx := NumGet( this.mib_addr+1320, "Int64" )
		
		; On first call there isnt any meaningful information 
		if (this.timestamp == 0)
		{
			this.timestamp:= this.GetCurrentSystemTime()
			return -2
		}
		
		; Return stats starting with the second method call
		OldTimestamp:= this.timestamp
		this.timestamp:= this.GetCurrentSystemTime()
		
		RxBPS := Round( ( ( Rx-OldRx ) / 1000 ) / ( (this.timestamp - OldTimestamp) /1000 ) * 1000 )
		TxBPS := Round( ( ( Tx-OldTx ) / 1000 ) / ( (this.timestamp - OldTimestamp) /1000 ) * 1000 ) 
		
		return 0
	}
	
	/*
	Create the MIB struct and set all values to Zero. 
	Return pointer to MIB struct.
	*/
	CreateMIB_IFROW2()
	{
		Local addr:=0
		this.SetCapacity( "MIB_IF_ROW2", 1368 )
		addr:= this.GetAddress("MIB_IF_ROW2")
		this.SetToZero(addr, 1368)
		return addr
	}
	
	/*
	Set length bytes starting from addr to Zero.
	*/
	SetToZero(addr, length:=1368)
	{
        DllCall( "RtlFillMemory", "Ptr",addr, "Ptr",length, "UChar",0)
	}
	
	/*
	Return the index of the most likely used interface.
	*/
	GetBestInterface()
	{
	Local index:=0
		DllCall( "iphlpapi\GetBestInterface", "Ptr",0, "PtrP",index )
		if (!index)
		{
			MsgBox, 48, Warning, Could not get best interface. , 3
			return 0
		}
		return index
	}
	
	/*
	Get the index of an interface by name.
	Returns negative value on error.
	Returns matching interface id on success.
	*/
	GetInterfaceByName(name)
	{
		Local interfaceCount, interfaceName
		; Get number of current interfaces
		DllCall( "iphlpapi\GetNumberOfInterfaces", "PtrP",interfaceCount )	
		
		; Loop over each interface and check if it's name matches %name%
		Loop % interfaceCount
		{
			; Reset InterfaceLuid
			NumPut( 0, this.mib_addr, "Int64" )
			; Put current Interface ID into MIB struct
			NumPut( A_Index, this.mib_addr+8 , "UInt")
			; Get Network information for the selected Interface ID
			DllCall( "iphlpapi\GetIfEntry2", "Ptr", this.mib_addr)
			; Check if the interface name matches the target name
			interfaceName:= StrGet( this.mib_addr+542, "UTF-16" )
			if (interfaceName == name)
			{
				return A_Index
			}
		}
		return -1
	}
	
	/*
	Get the current System time in order to calculate bytes per second.
	The information is in Coordinated Universal Time (UTC) format.
	*/
	GetCurrentSystemTime()
	{
		Local timestamp
		ErrorLevel:= DllCall( "GetSystemTimeAsFileTime", "Int64P",timestamp)
		return timestamp // 10000
	}
}

































