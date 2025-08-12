# Insights Inventory Extension Release Notes

_Applies to: Patch My PC Advanced Insights Inventory Extension_

Details the production release history for Patch My PC's Advanced Insights **InventoryExtensions.msi**, the most recent release being shown first.

### 1.7.0- 2025-07-30

* Fixed bug where strings with non standard UTF8 chars prevented monitor display table from loading.
* Improved uninstallation logic when uninstalling/upgrading MSI from an unhealthy state.

### 1.6.3- 2025-04-16

* Fixed Possible null reference bug across PMPC\_UserProfile, PMPC\_UserApps and PMPC\_BrowserExtension classes.
* Updated Dependencies.

### 1.6.2- 2025-01-13

* Various bug fixes to PMPC\_BrowserExtension.&#x20;
* ESR versions of firefox now supported.
* Latest versions of Opera now supported.
* Chromium based policies that make use of "Secure Preferences" now supported.

### 1.6.0- 2024-11-26

* Notifications sent from Advanced Insights will now be displayed with custom branding, as configured in Software Center

### 1.5.5- 2024-11-06

* Updated dependencies.
* PMPC\_BrowserExtension data now more accurate. Chromium based browsers with multiple profiles configured now have all extensions inventoried across all profiles.&#x20;
* Fixed bug causing Brave Browser extensions to be missed.

### 1.5.3- 2024-08-29

* Fixed PMPC\_Update bug for Windows Server 2016 & 2019.
* Servers now only scan against Windows Update services and not Microsoft Update

### 1.5.2 - 2024-05-29

* Fixed PMPC\_UserProfile bug for file paths exceeding 260 characters
* Fixed PMPC\_BrowserExtension bug for invalid extension JSON files.
* Now targeting .NET 4.6.2 for better Windows Server support&#x20;

### 1.5.0 - 2024-04-29

* Better installer experience & logic
* More accurate user profile enumeration
* PMPC\_BrowserExtension now has an Chrome/Edge store ID property
* Fixed bug that caused only 1 browser extension to be inventoried from Firefox
* Fixed "Invalid Disk" bug on PMPC\_Disks enumeration

### 1.4.0 - 2024-03-13

#### New:

* PMPC\_WifiInterface
* PMPC\_UserProfile

#### Improved:

* PMPC\_BrowserExtension: Now supports more locales.
* PMPC\_LocalGroups: Added "GroupMember" property to distinguish between users and group members.

### Removed:

* PMPC\_UserRights

### 1.3.2 - 2024-02-22

* Improved User-Installed App Inventory&#x20;
* ODBC Inventory now excludes the default "Visio Database Samples" connection.
* All PowerShell scripts removed from Installer

### 1.3.1 - 2024-02-14

* Further improvements to PMPC\_Dock

### 1.3.0 - 2024-01-25

#### Bug Fixes:

* PMPC\_Dock improved detection method
* PMPC\_Monitors now supports more HP monitors

#### New Inventory Class:

* PMPC\_BrowserExtension

### 1.2.0 - 2024-01-18

Initial release of InventoryExtensions.msi

Supports the following report classes:

* PMPC\_Batteries
* PMPC\_Disks
* PMPC\_Dock
* PMPC\_LocalGroups
* PMPC\_Monitors
* PMPC\_UserApps
* PMPC\_UserRights
* PMPC\_ODBC
* PMPC\_Updates
