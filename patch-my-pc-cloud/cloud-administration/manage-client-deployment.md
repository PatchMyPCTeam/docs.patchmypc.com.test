# Manage Client Deployment

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote is-important">
<p>This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.</p>
<p>Please do not share links to these docs with others outside of the Private Preview.</p>
<p>Once this feature is released, it will be announced and this banner removed.</p>
</blockquote>

The Patch My PC (PMPC) _Client_ allows you to retrieve data from a computer enrolled to Intune and report it back to your PMPC Cloud company. This data can then be viewed and worked with as part of the [Reporting](../cloud-reporting/) feature.

This document contains the following sections:

* [PMPC Client Prerequisites](manage-client-deployment.md#pmpc-client-prerequisites)
* [Install the PMPC Client](manage-client-deployment.md#install-the-pmpc-client)
* [Uninstall the PMPC Client](manage-client-deployment.md#uninstall-the-pmpc-client)
* [Update the PMPC Client](manage-client-deployment.md#update-the-pmpc-client)

### PMPC Client Prerequisites

Before installing the Client, ensure:

1. You are using the PMPC Portal and it is connected to your [Intune tenant](manage-your-environments-in-cloud/manage-cloud-intune-tenants.md#connecting-to-an-intune-tenant).
2. Your PMPC company is connected to the same Intune tenant that is used to manage the devices from which you want to gather your reporting data.
3. You are using PMPC Cloud to deploy and manage your third-party apps, updates and Custom Apps.
4. You have installed the correct version of the [.NET 8 Desktop Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) on any devices on which you want to install the agent.

<blockquote class="wp-block-quote is-important">
<p>The PMPC Client requires .NET version 8 specifically. It cannot use later versions.</p>
</blockquote>

### Install the PMPC Client

To install the Patch My PC (PMPC) Client:

1. Navigate to **Settings | Client Deployment**

![Navigating to "Settings | Client Deployment"](/_images/image-(2724).png "Navigating to “Settings | Client Deployment”")

The **Client Deployment** screen is shown, which is split into two sections:

* **Preview Version Deployment –** Shows details of the preview version of our Client and which Entra ID groups it is targeted to (if relevant).
* **Production Version Deployment -** Shows details of the production version of our Client and which Entra ID groups it is targeted to (if relevant).

!["Client Deployment" screen](/_images/image-(2725).png "“Client Deployment” screen")

2. To deploy the Client (**Preview** or **Production**), click the **Groups** dropdown and select the relevant Entra ID group(s) you want to deploy the Client to.

<blockquote class="wp-block-quote is-note">
<p>We recommend deploying the PMPC Client to a pilot group of devices first to ensure no issues arise.</p>
<p>See <a href="https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/groups-add">Add groups to organize users and devices</a> for more details on creating and working with groups in Intune.</p>
</blockquote>

![Selecting the Entra ID Group(s) you want to deploy the client to](/_images/image-(2726).png "Selecting the Entra ID Group(s) you want to deploy the client to")

3. Click **Save**

![Clicking "Save"](/_images/image-(2727).png "Clicking &#x22;Save&#x22;")

The **Success** notification is shown.

!["Success – Created" notification](/_images/image-(2728).png "“Success – Created” notification")

Once the Win32 app for the Client has been created in Intune, the status updates to **Success** and the Client will be deployed to the targeted devices.

![Client deployed successfully](/_images/image-(2729).png "Client deployed successfully")

As the Client is installed on the targeted devices, the number of **Devices Managed** shown in the **Dashboard** will increase.

<blockquote class="wp-block-quote is-tip">
<p>You can also check for the existence of the **C:\ProgramData\Patch My PC\Agent** folder on any target devices and review the **C:\Windows\Temp\PatchMyPC.Client.log** to monitor the installation of the Client.</p>
</blockquote>

<blockquote class="wp-block-quote is-note">
<p>To deploy the Client to other Entra ID groups, select the relevant groups from the **Groups** dropdown and click **Save**. The **Success – Updated** notification will be displayed and the Client will be deployed to the additional groups.</p>
</blockquote>

### Uninstall the PMPC Client

To uninstall the Patch My PC (PMPC) Client you can:

* [Modify the Groups the Client is deployed to](manage-client-deployment.md#modify-the-groups-the-client-is-deployed-to)
* [Select specific groups to uninstall the client from](manage-client-deployment.md#select-specific-groups-to-uninstall-the-client-from)
* [Delete the Client deployment](manage-client-deployment.md#delete-the-client-deployment)

#### Modify the Groups the Client is deployed to

You can uninstall the Client by following the [Install the PMPC Client](manage-client-deployment.md#install-the-pmpc-client) process, but instead of adding a group to the **Groups** dropdown, remove the relevant group(s) you want to uninstall the Client from and click **Save**.

Once you click **Save**, the Client will be uninstalled from any devices in the Entra ID group(s) you just removed.

#### Select specific groups to uninstall the client from

You may have a scenario where the Client has been deployed to Entra ID groups not included in your current Client deployment.

In this scenario, you can also uninstall the Client by:

1. Clicking the relevant **Uninstall Client** button.

![Clicking the relevant "Uninstall Client" button](/_images/image.png "Clicking the relevant \"Uninstall Client\" button")

2. Select the relevant group.

![Clicking the relevant "Uninstall Client" button](/_images/image-(1).png "Clicking the relevant “Uninstall Client” button")

<blockquote class="wp-block-quote is-note">
<p>If a group is greyed out, it means the current Client deployment is targeted to that group, and you should use the [Modify the Groups the Client is deployed to](manage-client-deployment.md#modify-the-groups-the-client-is-deployed-to) process instead.</p>
</blockquote>

3. Add any additional Groups as required.
4. Click **Save**.

![Clicking "Save"](/_images/image-(2).png "Clicking “Save”")

The **Client Deployment** page is displayed along with the **Success – Updated** notification.

!["Success | Updated" notification](/_images/image-(3).png "“Success | Updated” notification")

The Client will then be uninstalled from all the devices within the selected Entra ID Group(s).

#### Delete the Client deployment

If you want to delete the entire deployment used to deploy the Client:

1. Click the red trash can beside the relevant Client version whose deployment you wish to delete.

![Clicking the red trash can beside the relevant Client version whose deployment you wish to delete](/_images/image-(4).png "Clicking the red trash can beside the relevant Client version whose deployment you wish to delete")

2. On the **Are you sure?** dialog box, click **Submit**

![Clicking "Submit" on the "Are you sure?" dialog](/_images/image-(5).png "Clicking “Submit” on the “Are you sure?” dialog")

The **Client Deployment** screen is redisplayed along with the **Success – Deleted** notification.

!["Client Deployment" screen is redisplayed along with the "Success – Deleted" notification](/_images/image-(6).png "“Client Deployment” screen is redisplayed along with the “Success – Deleted” notification")

<blockquote class="wp-block-quote is-important">
<p>Using this option will only delete the deployment from Intune. It will not uninstall the Client from any of the devices targeted by the current deployment.</p>
<p>Also, as the **Client Deployment** screen does not currently refresh, you will need to refresh it to see any updates.</p>
</blockquote>

### Update the PMPC Client

When a new version of our Client is released, any existing Clients will be automatically updated.