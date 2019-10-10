#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#Include NetWorkAnalyzer.ahk


Net:= new NetWorkAnalyzer("Realtek PCIe GbE Family Controller")
Net.GetNetworkSpeed(Rx, Tx, RxBPS, TxBPS)


; Example: A simple input-box that asks for first name and last name:

Gui, Add, Text,w200 h50 vVar , RxBPS: %RxBPS% | TxBPS: %TxBPS%
Gui, Add, Button, default, OK  ; The label ButtonOK (if it exists) will be run when the button is pressed.
Gui, Show,, Simple Input Example
Loop
{
	Net.GetNetworkSpeed(Rx, Tx, RxBPS, TxBPS)
	GuiControl, , Var,  RxBPS: %RxBPS% | TxBPS: %TxBPS%
	Sleep, 500
}
return  ; End of auto-execute section. The script is idle until the user does something.

GuiClose:
ButtonOK:
ExitApp