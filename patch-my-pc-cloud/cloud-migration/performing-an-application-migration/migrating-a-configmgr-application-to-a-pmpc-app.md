# Migrating a ConfigMgr application to a PMPC App

_Applies to: Patch My PC Cloud_

{% hint style="danger" %}
**Important**

This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.

Please do not share links to these docs with others outside of the Private Preview.

Once this feature is released, it will be announced and this banner removed.
{% endhint %}

ConfigMgr applications that can be migrated to Patch My PC (PMPC) Cloud and deployed as one of our apps have a **Match Type** of **PMPC App**.

Once you click **Migrate** to migrate a ConfigMgr application to a PMPC App, the Deployment Wizard starts, and you can follow the [Deploying an App using Cloud](../../cloud-deployments/deploying-an-app-using-cloud/) section, but please note the following:

* As a double-check, you should check that the information on each tab is correct before clicking **Next**.
* On the **Configurations** tab, under the **Install Parameters** tool/section, check that the **Additional Argument** field is correct and includes any required additional arguments/command line options.
* On the **Assignments** tab, you can click **ConfigMgr Assignment List** to see a list of the current assignments in ConfigMgr, so you can then review this and set these up in Intune accordingly.

{% hint style="danger" %}
**Important**

In Private Preview, we are not matching ConfigMgr groups, assignments and Collections to Entra ID groups. You will need to manually configure your assignments.
{% endhint %}

{% hint style="success" %}
**Tip**

If you don’t want to deploy this app now, just click **Install App** under **App Without Assignments** on the **Assignments** tab, then click **Migrate** to just create the app in Intune. When you are ready, you can edit the Deployment and add the required Assignment types.
{% endhint %}

Once you have added your assignments, click **Migrate** and the **Success – Deployment Created, Migration Pending** notification is shown.

<figure><img src="../../../.gitbook/assets/image (10).png" alt="“Migrate, the Success – Deployment Created, Migration Pending” notification" width="563"><figcaption></figcaption></figure>

The **Status** field also updates to show **In Progress** as the deployment is being created, with any required content (such as extra files) being zipped and sent to Azure Blob Storage.

You can also monitor the progress of the deployment by clicking the **Deployments** node and watching for the **Status** of the deployment to change to **Success**.

<figure><img src="../../../.gitbook/assets/image (11).png" alt="Monitoring the status of the deployment" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

To see the migrated app in Intune, within the Microsoft Intune admin center navigate to:

**Home > Apps | Windows > Windows | Windows Apps > <**_**app\_name**_**>**

![Migrated app in Intune](<../../../.gitbook/assets/image (12).png>)
{% endhint %}
