# Advanced Insights Log Collector

_Applies to: Patch My PC Advanced Insights_

Sometimes we need you to provide log files, including information about your Advanced Insights instance. Your Advanced Insights deployment includes the Log Collector executable that can be used to collect all required logs.

{% hint style="info" %}
**Note**

The Advanced Insights Log Collector is located at:

_`%Advanced Insights Install Directory%`_`\Api\LogCollector\AdvancedInsightsLogDiag.exe`\


For example:

`C:\Program Files (x86)\Advanced Insights\Api\LogCollector\AdvancedInsightsLogDiag.exe`
{% endhint %}

{% hint style="info" %}
The Log Collector can be executed manually and is also used within the Advanced Insights installer. Once the log collection process is completed, a zip file is created on the desktop called:

**AdvancedInsights\_Diag\_xxxxxxxx\_xxxxxx.zip**

This ZIP should be shared with Patch My PC technical support.

_Example output:_
{% endhint %}

<figure><img src="../_images/gitbook/image%20%281926%29.png" alt=""><figcaption><p>Advanced Insights log collection output.</p></figcaption></figure>

**This page provides details about what information the AdvancedInsightsLogDiag.exe collects.**

### Advanced Insights data and installation logs

The contents of the following directory are collected, which consist of the 'AdvancedInsightsApi.log' and any 'AdvInsights\_Verx.x.x.zip' installer logs.

C:\ProgramData\AdvancedInsights\Logs

<figure><img src="../_images/gitbook/image%20%281924%29.png" alt=""><figcaption><p>Advanced Insights default logging directory</p></figcaption></figure>

### Windows Application Event Log

The Windows Application Event log data is collected and output into 'Application\_EventLog.log' with a filter applied for the following event sources:

* ".NET Runtime"&#x20;
* "Advanced Insights"
* "MsiInstaller" - if required to diagnose install problems, the filter will include&#x20;

### Advanced Insights SQLite db

The 'ConfigManagerLocation' and 'ConfigManagerDatabase' value are collected from the Advanced Insights SQLite database file located at:

**'C:\ProgramData\AdvancedInsights\Data\Api\AdvancedInsightsConfig.db'**

### SQL Server information

The following information is queried from the SQL Server instance where the Configuration Manager database is located:\
\
**SQL Master db:**

* Configuration Manager database name
* &#x20;Configuration Manager databaste state (ONLINE/OFFLINE)
* Configuration Manager database compatibility level
* Configuration Manager database .mdf file path
* Configuration Manager database file size
* Configuration Manager database log file .ldf path
* Configuration Manager database log file size
* SQL Server version
* SQL Server Product Level
* SQL Server Edition
* SQL Server Engine Edition
* SQL Server Product build
* SQL Server Product Major version
* SQL Server Product minor version
* SQL Server Product update version
* SQL Server Installed updates
* SQL Server remote query timeout value
* SQL Server maximum degree of parallelism value
* SQL Server Minimum size of server memory (MB)
* SQL Server Maximum size of server memory (MB)

**Configuration Manager SQL database:**

* Advanced Insights Inventory Extensions class names and data counts.
* Advanced Insights Inventory Extensions Configuration Manager application information. For    example 'Name', 'created date', 'version', 'number of deployments'.
* Configuration Manager database level SQL configured properties:
  * MAXDOP
  * LEGACY\_CARDINALITY\_ESTIMATION
  * PARAMETER\_SNIFFING
  * QUERY\_OPTIMIZER\_HOTFIXES

### Windows Server IIS information

* Information related to the Advanced Insights IIS websites and application pools are collected.
* Advanced Insights Api
* Advanced Insights Frontend
* Website name
* HTTPS bindings included the current SSL certificate properties

### Windows Server information

* The version of Advanced Insight currently installed.
* The install date of Advanced Insights.
* The install path of Advanced Insights.
* The install source of Advanced Insights.
* Server CPU properties.
* Installed Server RAM
* Server disks including total size and free space
* Windows OS version
* Check for Server pending restart.
* List Windows updates installed in the last 30 days.
