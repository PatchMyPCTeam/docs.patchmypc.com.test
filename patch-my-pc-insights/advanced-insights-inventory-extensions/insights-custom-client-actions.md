# Insights Custom Client Actions

_Applies to: Patch My PC Advanced Insights_

{% hint style="warning" %}
Advanced Insights must be granted the correct permissions to your SMS Provider for these actions to work. See [Configuration Manager Permissions](../insights-configuration-manager-permission-requirements.md).
{% endhint %}

Clients with the Inventory Extensions MSI installed will support the use of our custom client actions:

![](<../../.gitbook/assets/ClientActions (2).png>)

### ⚙ Script Approval

If you see this message when using any of the custom client actions:

![](../../.gitbook/assets/image-\(968\).png)

This means you have the "Additional Script Approver" setting enabled in ConfigMgr. To approve our script, please follow these steps:

![](<../../.gitbook/assets/script-approval (1).png>)

1. Open your ConfigMgr Console
2. Go to Software Library > Scripts
3. Right click and approve the "Advanced Insights Client Actions" script

### Custom Action Descriptions

* Notify - Sends a message box to all users logged in on the client, this message includes the\
  ![](../../_images/image-\(2261\).png%3E)
* Install Updates - Installs all updates which are advertised to the device which are targeted as available or required. This is the same action as pressing Install All in the Software Center.
* Repair Client - Executes the ccmrepair.exe
* Clear CCM Cache - Clears all ccmcache items on the client (including persistent cache)
