---
description: Advanced Insights welcome page
---

# Using Insights for the first time

_Applies to: Patch My PC Advanced and Patch Insights_

{% hint style="info" %}
The default credentials for your first logon are below. You will be prompted to change these:

* Username: admin
* Password: 123qwe
{% endhint %}

On first logon, you will see the welcome page. You can access this page any time by clicking your username in the top right of the screen.&#x20;

![](/_images/image-(1209).png "Advanced Insights welcome screen")

The welcome screen needs your Patch My PC license key and your ConfigMgr site server details.

### License Key

If Advanced Insights is installed on the same server as the Patch My PC Publisher we will read the license key automatically. Alternatively, please add your license key and click to verify.&#x20;

![](/_images/image-(1109).png "")

### Configuration Manager Database Details

Provide the server name and database name of your ConfigMgr primary site and click to connect.

As long as the IIS application pool identity running the Advanced Insights Controller website has permission to read the database, you should be good to go.&#x20;

If you have a problem at this stage, please see [this document ](insights-sql-permission-requirements.md)for details on granting SQL permissions.

![](/_images/image-(1106).png "")

Once the license key and SQL sections are successfully completed, click **Go to Dashboard** in the final step to complete setup.

![](/_images/image-(1138).png "")