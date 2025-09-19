# Overview of Cloud Reporting

_Applies to: Patch My PC Cloud_

{% hint style="danger" %}
**Important**

This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.

Please do not share links to these docs with others outside of the Private Preview.

Once this feature is released, it will be announced and this banner removed.
{% endhint %}

The _Reporting_ feature of Patch My PC (PMPC) Cloud allows you to see a wealth of information about your organization that you can use to monitor, maintain, and enhance your environment.

The **Reporting** node consists of the following sub-nodes, each of which contains the most common datasets organizations typically want to report on:

* **Dashboard -** Contains a summary of all of the information from the other tabs.
* **Software Updates -** Contains a summary of the most common software update-related information.
* **Hardware -** Contains a summary of the most common hardware-related information.
* **Intune  -** Contains a summary of the most common information from your Intune tenant.

{% hint style="info" %}
**Note**

The sub-nodes you see are determined by the license your PMPC Cloud company is running:

* **Enterprise Plus -** You will only see the **Intune** sub-node.
* **Enterprise Premium –** You will see all sub-nodes.
{% endhint %}

{% hint style="danger" %}
**Important**

The data in the **Intune** sub-node is populated using Microsoft Graph calls to your Intune tenant.

For data to appear and update in the other Reporting sub-nodes, you need to install our client on any devices you wish to collect data from. See [Patch My PC Client](../cloud-administration/manage-client-deployment.md) for more information.
{% endhint %}

See [Working with Cloud Reporting](working-with-cloud-reporting.md) for more details on working with the data presented by the Reporting feature.
