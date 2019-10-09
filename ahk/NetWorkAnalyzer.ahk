/*
This class provides access to the network connection and data.
This is a wrapper around the Ip-Helper-Api-DLL (Iphlpapi.dll).
Nearly every functionality is based on the MIB_IFROW2  Struct.

__________________________________________________________________________________________
 
  STRUCTURE MIB_IFROW2 ( MSDN http://goo.gl/Fufv7m )
  ----------------------------------------------------------------------------------------
  Offset Size Type   Description                     Comment
  ----------------------------------------------------------------------------------------
  0        8  INT64  InterfaceLuid 
  8        4  UINT   InterfaceIndex
  12      16  GUID   InterfaceGuid
  28     514  WSTR   Alias   
  542    514  WSTR   Description                     Friendly name
  1056     4  UINT   PhysicalAddressLength
  1060    32  BYTE   PhysicalAddress                 MAC address
  1092    32  BYTE   PermanentPhysicalAddress        MAC address
  1124     4  UINT   Mtu
  1128     4  UINT   Type ( IFTYPE )
  1132     4  UINT   TunnelType
  1136     4  UINT   MediaType
  1140     4  UINT   PhysicalMediumType
  1144     4  UINT   AccessType   
  1148     4  UINT   DirectionType
  1152     4  UINT   InterfaceAndOperStatusFlags
  1156     4  UINT   OperStatus
  1160     4  UINT   AdminStatus
  1164     4  UINT   MediaConnectState
  1168    16  GUID   NetworkGuid
  1184     4  UINT   ConnectionType
  1188     4  ----   ----                            Padding for x64 alignment
  1192     8  UINT64 TransmitLinkSpeed
  1200     8  UINT64 ReceiveLinkSpeed
  1208     8  UINT64 InOctets                        Received Bytes
  1216     8  UINT64 InUcastPkts
  1224     8  UINT64 InNUcastPkts
  1232     8  UINT64 InDiscards
  1240     8  UINT64 InErrors
  1248     8  UINT64 InUnknownProtos
  1256     8  UINT64 InUcastOctets                   Received bytes
  1264     8  UINT64 InMulticastOctets
  1272     8  UINT64 InBroadcastOctets
  1280     8  UINT64 OutOctets                       Sent Bytes
  1288     8  UINT64 OutUcastPkts
  1296     8  UINT64 OutNUcastPkts
  1304     8  UINT64 OutDiscards
  1312     8  UINT64 OutErrors
  1320     8  UINT64 OutUcastOctets                  Sent Bytes
  1328     8  UINT64 OutMulticastOctets
  1336     8  UINT64 OutBroadcastOctets
  1344     8  UINT64 OutQLen
  ----------------------------------------------------------------------------------------
  1352 bytes in total + 16 extra bytes follow
  ----------------------------------------------------------------------------------------
  1352     8  PTR    Pointer to InUcastOctets
  1360     8  PTR    Pointer to OutUcastOctets             
  ----------------------------------------------------------------------------------------

*/
class NetworkAnalyzer ; Author: Leon Morten Richter
{
	
	/*
	Create a new instance of NetworkAnalyzer.
	*/
	__New()
	{
		; Load library for better performance
		this.lib := DllCall( "LoadLibrary", "Str","Iphlpapi.dll", "Ptr" )
		if (!this.lib)
		{
			MsgBox, 48, Warning, Could not load Iphlpapi.dll. , 3
		}
		; Create MIB Struct and set all values to zero
		this.mib_addr:= this.CreateMIB_IFROW2()
		
		; Set the interface | TODO: add the possibility to set interface by name
		this.interfaceId:= this.GetBestInterface()
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
	*/
	GetNetworkStatus()
	{
		OldRx := NumGet( this.mib_addr+1256, "Int64" )
		OldTx := NumGet( this.mib_addr+1320, "Int64" )
		
		;Call DLL and store the result inside our MIB struct
		ErrorLevel:= DllCall( "iphlpapi\GetIfEntry2", "Ptr", this.mib_addr)
		if (ErrorLevel)
		{
			this.SetToZero(this.mib_addr)
			return 0
		} 
		
		NewRx := NumGet( this.mib_addr+1256, "Int64" )
		NewTx := NumGet( this.mib_addr+1320, "Int64" )
		
		MsgBox, %OldRx% | %OldTx% | %NewRx% | %NewTx%
		return 10
	
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
	*/
	GetInterfaceByName(name)
	{
	}
	
	
}

































