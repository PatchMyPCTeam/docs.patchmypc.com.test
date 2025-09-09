---
description: Definition and technical description of each of our custom WMI Classes
---

# Insights WMI Class Definitions

_Applies to: Patch My PC Advanced Insights_

<blockquote class="wp-block-quote">
<p><mark style="color:yellow;"><strong>Properties marked with \</strong>*</mark></p>
<p><mark style="color:yellow;">These properties can vary by hardware manufacturer. Data generation methods may differ between manufacturers and not all manufacturers may be supported. Users should consult the manufacturer's documentation for accurate interpretation of these properties where applicable.</mark></p>
</blockquote>

<strong>*

### PMPC\_Disks

</strong>DeviceID:<strong> Identifier that uniquely names the physical disk.

</strong>BusType:<strong> The interface the disk is connected by.

</strong>MediaType:<strong> Media type of the physical disk

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>Manufacturer:<strong> The name of the manufacturer

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>HealthStatus:<strong> A high-level indication of device health.

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>OperationalStatus:<strong> Status further explaining a given health status.

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>Model:<strong> This field represents the model number of the hardware

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>PowerOnHours:<strong> Length of time, in hours, the storage device has been powered on since manufacture.

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>ReadErrorsTotal:<strong> Total read errors encountered by the device.

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>SerialNumber:<strong> Serial Number of the battery

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>Temperature:<strong> The current temperature of the storage device in Celsius

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>TemperatureMax:<strong> The maximum temperature in Celsius at which the storage device is capable of normal operation.

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>Wear:<strong> Storage device wear indicator, in percentage. At 100 percent, the estimated wear limit will have been reached.

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>WriteErrorsTotal:<strong> Total write errors encountered by the device.

<mark style="color:yellow;">These properties are collected via SMART. Not all devices may support SMART monitoring</mark>

</strong>*

### PMPC\_Batteries

<strong>BatteryID:</strong> String identifying the battery.

<strong>DesignCapacity:</strong> The design capacity of the battery in milliwatt-hours.&#x20;

<strong>FullChargeCapacity:</strong> The full charge capacity of the battery in milliwatt-hours.&#x20;

<strong>Health:</strong> Comparison of the FullChargeCapacity to the DesignCapacity property is used to determine the health of the battery. (100 = Healthy)

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>Chemistry:</strong> Describes the batteries chemistry.

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>Manufacturer:</strong> The name of the manufacturer

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>ManufacturerDate:</strong> The date the battery was manufactured

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>SerialNumber:</strong> Serial Number of the battery

<strong>*

### PMPC\_ODBC

</strong>DataSourceName:<strong> Name of the ODBC

</strong>Database:<strong> The Display Name of the Application

</strong>Description:<strong> The reported version of the application.

</strong>Driver:<strong> The driver used for the ODBC

</strong>DriverVersion:<strong> The specific file version of the driver

</strong>Platform:<strong> Specifies whether the ODBC is 64/32 bit

</strong>User:<strong> The name of the user that owns the ODBC (if applicable).

</strong>*

### PMPC\_UserApps

<strong>InstallLocation:</strong> The folder location in which the application is installed

<strong>DisplayName:</strong> The Display Name of the Application

<strong>DisplayVersion:</strong> The reported version of the application.

<strong>InstallDate:</strong> The date the application was installed.

<strong>Publisher:</strong> The name of the publisher of the application.

<strong>QuietUninstallString:</strong> command line string to uninstall the application.

<strong>UninstallString:</strong> command line string for silent uninstall of the application.

<strong>User:</strong> The name of the user that installed the application.

<strong>*

### PMPC\_LocalGroups

</strong>GroupName:<strong> Name of the local group.

</strong>Members:<strong> List of user members belonging to that local group.&#x20;

</strong>GroupMembers:<strong> List of sub groups that are members of the local group

<mark style="color:yellow;">If a member cannot be identified the SID will be displayed instead.</mark>

</strong>*

### PMPC\_Dock

<blockquote class="wp-block-quote">
<p>Please note that collection of this data requires additional software from the vendors to be installed on clients:</p>
<p>* HP - <a href="https://www.hp.com/us-en/solutions/client-management-solutions/download.html">HP Dock Accessory Provider</a></p>
<p>* Lenovo - <a href="https://pcsupport.lenovo.com/us/el/solutions/ht037099">Lenovo Dock Manager</a></p>
<p>* DELL - <a href="https://www.dell.com/support/kbdoc/en-us/000177080/dell-command-monitor">Dell Command Monitor</a> (or DSIA)</p>
</blockquote>

<strong>DeviceName:</strong> Identified name of the dock device.

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>Firmware:</strong> The firmware version currently installed on the dock

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>Manufacturer:</strong> Manufacturer of the dock

<mark style="color:yellow;"><strong>\</strong>*</mark><strong>SerialNumber:</strong> Serial Number of the dock if applicable (For dell this is the same as service tag)

<strong>PnPID:</strong> Device "PnP" Id, this is only used if we werent able to identify the dock model

<strong>*

### PMPC\_Monitors

</strong>InstanceName:<strong> Unique Identifier for the monitor

</strong>DeviceName:<strong> Name of the monitor

</strong>InchSize:<strong> Diagonal size of monitor

</strong>ConnectionType:<strong> The cable used to connect to monitor

</strong>Primary:<strong> Whether this monitor is configured as the primary display. True or False.&#x20;

</strong>ResolutionHorizontal:<strong> Maximum horizontal pixel count

</strong>ResolutionVertical:<strong> Maximum vertical pixel count

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>Model:<strong> Model of the monitor

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>SerialNumber:<strong> Serial number of monitor (service tag for DELL)

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>Manufacturer:<strong> Name of manufacturer

<mark style="color:yellow;"></strong>\<strong>*</mark></strong>ManufactureYear:<strong> Year the monitor was made

</strong>*

### PMPC\_Updates

<strong>UpdateId:</strong> unique ID that represents the update

<strong>Title:</strong> Title of the update.

<strong>Status:</strong> Missing or Installed.

<strong>Service:</strong> The Update Service used to discover this update.

<strong>Product:</strong> Product associated with the update

<strong>ProductID:</strong> ProductID associated with the update

<strong>InstalledOn:</strong> Date the update was Installed On

<strong>DatePosted:</strong> Date the updated was release or revised

<strong>ArticleId:</strong> KB article ID identifying the update

<strong>*

### PMPC\_WifiInterface

</strong>GUID:<strong> unique ID that represents the Wifi Interface

</strong>Description:<strong> Name / description of the interface

</strong>Authentication:<strong> Type of authentication used (e.g., WPA2, WEP, Open)

</strong>Band:<strong> Frequency band used (e.g., 2.4GHz, 5GHz)

</strong>Channel:<strong> Current operating channel

</strong>Cipher:<strong> Encryption cipher used (e.g., AES, TKIP)

</strong>ConnectionMode:<strong> Mode of connection&#x20;

</strong>Driver Version:<strong> Version of the driver software controlling the interface

</strong>PhysicalAddress:<strong> MAC address of the interface

</strong>RadioType:<strong> Type of wireless radio (e.g., 802.11n, 802.11ac)

</strong>Signal:<strong> Percentage signal strength of the connection

</strong>SSID:<strong> Name of the wireless network

</strong>State:<strong> Current state of the interface (e.g., connected, disconnected)

</strong>*

### PMPC\_UserProfile

<strong>SID:</strong> Security Identifier associated with the user profile

<strong>Path:</strong> File path where the user profile is stored

<strong>LastLoggedIn:</strong> Date and time of the user's last login

<strong>AccountName:</strong> Name of the user account

<strong>SizeGB:</strong> Size of the user profile in gigabytes



<strong>*

### PMPC\_BrowserExtension

<blockquote class="wp-block-quote">
<p></strong>Note<strong></p>
<p>Supported Browsers:</p>
<p>* Chrome</p>
<p>* Edge</p>
<p>* Brave</p>
<p>* Firefox</p>
<p>* Opera</p>
</blockquote>

</strong>InstallPath:<strong> Path of the extension content and manifest

</strong>Name:<strong> Name of the extension

</strong>Author:<strong> The reported author of the browser extension acording to the manifest

</strong>Browser:<strong> The browser that the extension is installed in.

</strong>User:<strong> The user that has the extension installed. (All browser extensions are per user)

</strong>ID:<strong> ID of the Browser Extension associated with Chrome / Edge store

</strong>Version:** The version of the browser extension