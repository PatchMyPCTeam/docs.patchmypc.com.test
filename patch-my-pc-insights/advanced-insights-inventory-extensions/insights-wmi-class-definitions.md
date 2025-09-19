---
description: Definition and technical description of each of our custom WMI Classes
---

# Insights WMI Class Definitions

_Applies to: Patch My PC Advanced Insights_

> <mark style="color:yellow;">**Properties marked with \\**</mark><mark style="color:yellow;">\*</mark>
>
> <mark style="color:yellow;">These properties can vary by hardware manufacturer. Data generation methods may differ between manufacturers and not all manufacturers may be supported. Users should consult the manufacturer's documentation for accurate interpretation of these properties where applicable.</mark>

**\***

**PMPC\_Disks**

DeviceID: **Identifier that uniquely names the physical disk.**

BusType: **The interface the disk is connected by.**

MediaType: **Media type of the physical disk**

\<strong>\*Manufacturer: **The name of the manufacturer**

\<strong>\*HealthStatus: **A high-level indication of device health.**

\<strong>\*OperationalStatus: **Status further explaining a given health status.**

\<strong>\*Model: **This field represents the model number of the hardware**

\<strong>\*PowerOnHours: **Length of time, in hours, the storage device has been powered on since manufacture.**

\<strong>\*ReadErrorsTotal: **Total read errors encountered by the device.**

\<strong>\*SerialNumber: **Serial Number of the battery**

\<strong>\*Temperature: **The current temperature of the storage device in Celsius**

\<strong>\*TemperatureMax: **The maximum temperature in Celsius at which the storage device is capable of normal operation.**

\<strong>\*Wear: **Storage device wear indicator, in percentage. At 100 percent, the estimated wear limit will have been reached.**

\<strong>\*WriteErrorsTotal: **Total write errors encountered by the device.**

<mark style="color:yellow;">**These properties are collected via SMART. Not all devices may support SMART monitoring**</mark>

\*

### PMPC\_Batteries

**BatteryID:** String identifying the battery.

**DesignCapacity:** The design capacity of the battery in milliwatt-hours.

**FullChargeCapacity:** The full charge capacity of the battery in milliwatt-hours.

**Health:** Comparison of the FullChargeCapacity to the DesignCapacity property is used to determine the health of the battery. (100 = Healthy)

<mark style="color:yellow;">**\</strong>\***</mark>**Chemistry: Describes the batteries chemistry.**

<mark style="color:yellow;">**\</strong>\***</mark>**Manufacturer: The name of the manufacturer**<mark style="color:yellow;">**\</strong>\***</mark>**ManufacturerDate: The date the battery was manufactured**<mark style="color:yellow;">**\</strong>\***</mark>**SerialNumber: Serial Number of the battery\*PMPC\_ODBCDataSourceName: Name of the ODBCDatabase: The Display Name of the ApplicationDescription: The reported version of the application.Driver: The driver used for the ODBCDriverVersion: The specific file version of the driverPlatform: Specifies whether the ODBC is 64/32 bitUser: The name of the user that owns the ODBC (if applicable).\*PMPC\_UserAppsInstallLocation: The folder location in which the application is installedDisplayName: The Display Name of the ApplicationDisplayVersion: The reported version of the application.InstallDate: The date the application was installed.Publisher: The name of the publisher of the application.QuietUninstallString: command line string to uninstall the application.UninstallString: command line string for silent uninstall of the application.User: The name of the user that installed the application.\*PMPC\_LocalGroupsGroupName: Name of the local group.Members: List of user members belonging to that local group.GroupMembers: List of sub groups that are members of the local group**<mark style="color:yellow;">**If a member cannot be identified the SID will be displayed instead.**</mark>**\*PMPC\_DockPlease note that collection of this data requires additional software from the vendors to be installed on clients:\* HP -** [**HP Dock Accessory Provider**](https://www.hp.com/us-en/solutions/client-management-solutions/download.html)**\* Lenovo -** [**Lenovo Dock Manager**](https://pcsupport.lenovo.com/us/el/solutions/ht037099)**\* DELL -** [**Dell Command Monitor**](https://www.dell.com/support/kbdoc/en-us/000177080/dell-command-monitor) **(or DSIA)DeviceName: Identified name of the dock device.**<mark style="color:yellow;">**\</strong>\***</mark>**Firmware: The firmware version currently installed on the dock**<mark style="color:yellow;">**\</strong>\***</mark>**Manufacturer: Manufacturer of the dock**<mark style="color:yellow;">**\</strong>\***</mark>**SerialNumber: Serial Number of the dock if applicable (For dell this is the same as service tag)PnPID: Device "PnP" Id, this is only used if we werent able to identify the dock model\*PMPC\_MonitorsInstanceName: Unique Identifier for the monitorDeviceName: Name of the monitorInchSize: Diagonal size of monitorConnectionType: The cable used to connect to monitorPrimary: Whether this monitor is configured as the primary display. True or False.ResolutionHorizontal: Maximum horizontal pixel countResolutionVertical: Maximum vertical pixel count\<strong>\*Model: Model of the monitor\<strong>\*SerialNumber: Serial number of monitor (service tag for DELL)\<strong>\*Manufacturer: Name of manufacturer\<strong>\*ManufactureYear: Year the monitor was made\*PMPC\_UpdatesUpdateId: unique ID that represents the updateTitle: Title of the update.Status: Missing or Installed.Service: The Update Service used to discover this update.Product: Product associated with the updateProductID: ProductID associated with the updateInstalledOn: Date the update was Installed OnDatePosted: Date the updated was release or revisedArticleId: KB article ID identifying the update\*PMPC\_WifiInterfaceGUID: unique ID that represents the Wifi InterfaceDescription: Name / description of the interfaceAuthentication: Type of authentication used (e.g., WPA2, WEP, Open)Band: Frequency band used (e.g., 2.4GHz, 5GHz)Channel: Current operating channelCipher: Encryption cipher used (e.g., AES, TKIP)ConnectionMode: Mode of connectionDriver Version: Version of the driver software controlling the interfacePhysicalAddress: MAC address of the interfaceRadioType: Type of wireless radio (e.g., 802.11n, 802.11ac)Signal: Percentage signal strength of the connectionSSID: Name of the wireless networkState: Current state of the interface (e.g., connected, disconnected)\*PMPC\_UserProfileSID: Security Identifier associated with the user profilePath: File path where the user profile is storedLastLoggedIn: Date and time of the user's last loginAccountName: Name of the user accountSizeGB: Size of the user profile in gigabytes\*PMPC\_BrowserExtensionNoteSupported Browsers:\* Chrome\* Edge\* Brave\* Firefox\* OperaInstallPath: Path of the extension content and manifestName: Name of the extensionAuthor: The reported author of the browser extension acording to the manifestBrowser: The browser that the extension is installed in.User: The user that has the extension installed. (All browser extensions are per user)ID: ID of the Browser Extension associated with Chrome / Edge storeVersion:\*\* The version of the browser extension**
