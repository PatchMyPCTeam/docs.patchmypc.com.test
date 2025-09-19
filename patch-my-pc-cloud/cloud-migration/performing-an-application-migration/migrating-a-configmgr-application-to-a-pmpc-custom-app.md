# Migrating a ConfigMgr application to a PMPC Custom App

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.</p>
<p>Please do not share links to these docs with others outside of the Private Preview.</p>
<p>Once this feature is released, it will be announced and this banner removed.</p>
</blockquote>

ConfigMgr applications that can be migrated to Patch My PC (PMPC) Cloud and deployed as one of our Custom Apps have a **Match Type** of **Custom App**.

Once you click **Migrate** to migrate a ConfigMgr application to a PMPC Custom App, the Custom Apps Deployment Wizard starts, and you can follow the [Create a Custom App](../../custom-apps/create-a-custom-app/) section, but please note the following:

* As a double-check, you should check that the information on each tab is correct before clicking **Next**.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If the primary installer file is a .MSI, we auto-extract and populate the **Conflicting processes** field on the **General** tab.</p>
</blockquote>

* On the **Configurations** tab, under the **Install Parameters** tool/section, check that the **Additional Argument** field is correct and includes any required additional arguments/command line options.
* On the **Assignments** tab, you can click **ConfigMgr Assignment List** to see a list of the current assignments in ConfigMgr so you can then review this and set these up in Intune accordingly.

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>In Private Preview, we are not matching ConfigMgr groups, assignments and Collections to Entra ID groups. You will need to manually configure your assignments.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>If you don’t want to deploy this app now, just click **Install App** under **App Without Assignments** on the **Assignments** tab, then click **Migrate** to just create the app in Intune. When you are ready, you can edit the Deployment and add the required Assignment types.</p>
</blockquote>

* On the **Assignments** tab, if you do not want to set up any Detection Rules, you can click **Migrate**. If you do want to set up Detection Rules, you should click next to proceed to the **Detection Rules** tab.
* On the **Detection Rules** tab, you can either continue with the **Use Custom** option, i.e. what we detected in ConfigMgr, or select the **Patch My PC Default (Recommended)** option instead and let us use our recommended settings.

When you click **Migrate**, the **Success – Deployment Created, Migration Pending** notification is shown.

![“Migrate, the Success – Deployment Created, Migration Pending” notification](/_images/image-(7).png "“Migrate, the Success – Deployment Created, Migration Pending” notification")

The **Status** field also updates to show **In Progress** as the deployment is being created, with any required content being zipped (such as the primary installer file and any extra files) and sent to Azure Blob Storage.

You can also monitor the progress of the deployment by clicking the **Deployments** node and watching for the **Status** of the deployment to change to **Success**.

![Monitoring the status of the deployment](/_images/image-(8).png "Monitoring the status of the deployment")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>To see the migrated app in Intune, within the Microsoft Intune admin center navigate to:</p>
<p>**Home > Apps | Windows >Windows | Windows Apps ><**_**app\_name**_**>**</p>
<p>![Migrated app in Intune](/_images/image-(9).png>)</p>
</blockquote>