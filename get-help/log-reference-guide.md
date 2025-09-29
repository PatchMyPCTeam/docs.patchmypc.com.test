---
description: >-
  Sometimes we will need you to provide log files for troubleshooting. This
  guide will help you locate possible log files for different scenarios.
---

# Log Reference Guide

## Patch My PC Log Reference for Specific Scenarios

Below, you will find logs needed for specific scenarios.

## Server-Side Logs

### **Software Updates - Failing to Publish Updates Using Patch My PC's Publisher**

When using the Patch My PC **Publisher to published third-party updates to WSUS**, we will need the following log files from the SUP/WSUS server where the service is installed.

```
%PatchMyPCInstallDirectory%\PatchMyPC.log
%PatchMyPCInstallDirectory%\PatchMyPC.lo_
%PatchMyPCInstallDirectory%\Settings.xml
%PatchMyPCInstallDirectory%\PatchMyPC-DownloadHistory.csv
%PatchMyPCInstallDirectory%\PatchMyPC-PublishingHistory.csv
%SiteServerLogsFolder%\wsyncmgr*.log
%SiteServerLogsFolder%\WCM*.log
```

The following log may be needed **upon request only due to large file size**

```
%ProgramFiles%\Update Services\LogFiles\SoftwareDistribution.log
```

### **Software Updates - Failing to Publish Updates Using SCCM In-Console Publishing**

When using the **SCCM in-console publishing**, we will need the following log files from the SUP/WSUS server where the service is installed.

```
%SiteSystemLogsFolder%\SMS_ISVUPDATES_SYNCAGENT*.log
%SiteServerLogsFolder%\wsyncmgr*.log
%SiteServerLogsFolder%\WCM*.log
```

The following log file may be needed **upon request only due to large file size**

```
%ProgramFiles%\Update Services\LogFiles\SoftwareDistribution.log
```

### **SCCM Applications - Failing to Create/Update SCCM Applications Using Patch My PC's Publisher**

When using the Patch My PC **Publisher for SCCM application creation**, we will need the following log files to troubleshoot applications failing to create.

```
%PatchMyPCInstallDirectory%\PatchMyPC.log
%PatchMyPCInstallDirectory%\PatchMyPC.lo_
%PatchMyPCInstallDirectory%\Settings.xml
%PatchMyPCInstallDirectory%\PatchMyPC-DownloadHistory.csv
%PatchMyPCInstallDirectory%\PatchMyPC-PublishingHistory.csv
%SCCMInstallFolder%\Logs\SMSProv*.log
```

### **Intune Applications - Fails to Create/Update Applications Using Patch My PC's Publisher**

When using the Patch My PC **Publisher for Intune application creation**, we will need the following log files to troubleshoot applications failing to create.

```
%PatchMyPCInstallDirectory%\PatchMyPC.log
%PatchMyPCInstallDirectory%\PatchMyPC.lo_
%PatchMyPCInstallDirectory%\Settings.xml
%PatchMyPCInstallDirectory%\PatchMyPC-DownloadHistory.csv
%PatchMyPCInstallDirectory%\PatchMyPC-PublishingHistory.csv
```

## Client-Side Logs

### **Intune Applications/Updates Failing to Install on Client Devices**

When troubleshooting **Intune application installation errors on a client**, we will need multiple client logs. Please include the following logs:

```
%ProgramData%\PatchMyPCIntuneLogs\PatchMyPC-ScriptRunner.log
%ProgramData%\PatchMyPCIntuneLogs\PatchMyPC-SoftwareDetectionScript.log
%ProgramData%\PatchMyPCIntuneLogs\PatchMyPC-SoftwareUpdateDetectionScript.log
```

> \*\*Important\*\*
>
> For user-based apps, the logs mentioned above will reside in the following folders:
>
> \* %LocalAppData%\PatchMyPCIntuneLogs\PatchMyPC-Scriptrunner.log
>
> \* %Temp%\PatchMyPC-SoftwareDetectionScript.log
>
> \* %Temp%\PatchMyPC-SoftwareUpdateDetectionScript.log

```
%ProgramData%\Microsoft\IntuneManagementExtension\Logs\AgentExecutor.log
%ProgramData%\Microsoft\IntuneManagementExtension\Logs\IntuneManagementExtension.log
%ProgramData%\Microsoft\IntuneManagementExtension\Logs\Win32AppInventory.log
%ProgramData%\Microsoft\IntuneManagementExtension\Logs\AppWorkload.log
```

> \*\*Note\*\*
>
> Some Patch My PC log files listed above may be found in \*\*%WinDir%\CCM\*\* folder if that folder exists.

### **SCCM Applications Failing to Install on Client Devices**

When troubleshooting **SCCM application installation errors on a client**, we will need multiple client logs. Please include the following logs:

```
%WinDir%\CCM\Logs\AppDiscovery*.log
%WinDir%\CCM\Logs\AppEnforce*.log
%WinDir%\CCM\Logs\AppIntentEval*.log
%WinDir%\CCM\Logs\CAS*.log
%WinDir%\CCM\Logs\CIAgent.*log
%WinDir%\CCM\Logs\DataTransferService*.log
%WinDir%\CCM\Logs\PatchMyPC-ScriptRunner.log
%WinDir%\CCM\Logs\PatchMyPC-SoftwareDetectionScript.log
%WinDir%\CCM\Logs\StateMessage.log
```

### **Third-Party Software Updates Failing to Install on Client Devices**

When troubleshooting **update installation errors on a client**, we will need the following client logs:

```
%WinDir%\CCM\Logs\CAS*.log
%WinDir%\CCM\Logs\DeltaDownload*.log
%WinDir%\CCM\Logs\ScanAgent*.log
%WinDir%\CCM\Logs\StateMessage.log
%WinDir%\CCM\Logs\UpdatesDeployment*.log
%WinDir%\CCM\Logs\UpdatesHandler*.log
%WinDir%\CCM\Logs\UpdatesStore*.log
%WinDir%\CCM\Logs\DataTransferService*.log
%WinDir%\CCM\Logs\WUAHandler*.log
%WinDir%\CCM\Logs\PatchMyPC-ScriptRunner.log (If exist)
%WinDir%\WindowsUpdate.log
```

* You need to run [**Get-WindowsUpdateLog on Windows 8.1 and newer**](https://docs.microsoft.com/en-us/powershell/module/windowsupdate/get-windowsupdatelog?view=win10-ps) in PowerShell.

### **Download Stuck at 0% / Waiting to install / Preparing to download**

When troubleshooting **update installation errors on a client**, we will need the following client logs:

```
%WinDir%\CCM\Logs\CAS*.log
%WinDir%\CCM\Logs\CIAgent.*log
%WinDir%\CCM\Logs\ClientLocation*.log
%WinDir%\CCM\Logs\CMBITSManager*.log
%WinDir%\CCM\Logs\ContentTransferManager*.log
%WinDir%\CCM\Logs\DataTransferService*.log
%WinDir%\CCM\Logs\LocationServices.log*.log
%WinDir%\CCM\Logs\StateMessage.log
%WinDir%\CCM\Logs\UpdatesDeployment*.log
%WinDir%\CCM\Logs\UpdatesHandler*.log
%WinDir%\CCM\Logs\UpdatesStore*.log
%WinDir%\CCM\Logs\PatchMyPC-ScriptRunner.log (If exist)
```

## Configuration Manager Specific Logs

### **Automatic Deployment Rule Failing for Third-Party Updates**

When troubleshooting **automatic deployment rules failing for third-party updates**, we will need the following server-side logs. In this example, we will assume the main SCCM installation directory is: **C:\Program Files\Microsoft Configuration Manager**

* **C:\Program Files\Microsoft Configuration Manager\Logs\ruleengine\*.log**
* The [**PatchDownloader.log**](https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/log-files#BKMK_SU_NAPLog) (Location may vary)
  * C:\Program Files\SMS\_CCM\Logs\PatchDownloader\*.log (Most common location)
  * C:\Program Files\Microsoft Configuration Manager\Logs\PatchDownloader\*.log (Possible location)
  * %WinDir%\CCM\Logs (Possible location)
  * If **unable to locate** a current [**PatchDownloader.log**](https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/log-files#BKMK_SU_NAPLog), check HKLM\SOFTWARE\Microsoft\CCM\Logging\\@Global:**LogDirectory** on the [**site server**](https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/plan-for-site-system-servers-and-site-system-roles#configuration-manager-site-server)

![how to locate the patchdownloader.log file](../_images/locate-the-patchdownloader-log-file.png)

### **Updates Failing to Download to Deployment Package using SCCM Console**

When troubleshooting **updates failing to download into a deployment package from the SCCM console**, we will need the following log from the machine running the SCCM console:

```
%temp%\PatchDownloader*.log
```

> \*\*Note\*\*
>
> If you are using an RDP session, the \*\*patchdownloader.log\*\* may be in a numbered sub-folder in your \*\*Users\*\* \*\*%temp%\*\* folder.

### **Patch My PC Publisher - How to Enable Debug Logging**

Enabling Debug logging is often helpful for troubleshooting unique issues with publishing. Follow the steps below to enable Debug logging:

1. Open the Publisher
2. Click on the **General** tab
3. In the dropdown under **Logging Options** select **Debug**\
   ![Enable Debug Logging in Publisher](../_images/PatchMyPC-Settings_VB3O5uDPhE.png)\\
4. Close the Publisher
5. Open Services.msc and locate the **PatchMyPCService**
6. Right-click and Restart the **PatchMyPCService**
7. Debug Logging is now enabled

## List of Specific Patch My PC Logs and Files

### PatchMyPC.log

**PatchMyPC.log** is the primary log file for the Publisher and is often required by support for any troubleshooting. The file name and location are:

```
%PatchMyPCInstallDirectory%\PatchMyPC.log
%PatchMyPCInstallDirectory%\PatchMyPC.lo_
```

### **Settings.xml**

**Settings.xml** stores all settings related to the Publisher. This file is also used for [Backup and Restore](https://patchmypc.com/backup-and-restore-publisher-settings). The file name and location are:

```
%PatchMyPCInstallDirectory%\Settings.xml
```
