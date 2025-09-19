# Migrating a ConfigMgr application to a PMPC Custom App

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.</p>
<p>Please do not share links to these docs with others outside of the Private Preview.</p>
<p>Once this feature is released, it will be announced and this banner removed.</p>
</blockquote>

ConfigMgr applications that can be migrated to Patch My PC (PMPC) Cloud and deployed as one of our Custom Apps have a <strong>Match Type</strong> of <strong>Custom App</strong>.

Once you click <strong>Migrate</strong> to migrate a ConfigMgr application to a PMPC Custom App, the Custom Apps Deployment Wizard starts, and you can follow the [Create a Custom App](../../custom-apps/create-a-custom-app/) section, but please note the following:

* As a double-check, you should check that the information on each tab is correct before clicking <strong>Next</strong>.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If the primary installer file is a .MSI, we auto-extract and populate the <strong>Conflicting processes</strong> field on the <strong>General</strong> tab.</p>
</blockquote>

* On the <strong>Configurations</strong> tab, under the <strong>Install Parameters</strong> tool/section, check that the <strong>Additional Argument</strong> field is correct and includes any required additional arguments/command line options.
* On the <strong>Assignments</strong> tab, you can click <strong>ConfigMgr Assignment List</strong> to see a list of the current assignments in ConfigMgr so you can then review this and set these up in Intune accordingly.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>In Private Preview, we are not matching ConfigMgr groups, assignments and Collections to Entra ID groups. You will need to manually configure your assignments.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you don’t want to deploy this app now, just click <strong>Install App</strong> under <strong>App Without Assignments</strong> on the <strong>Assignments</strong> tab, then click <strong>Migrate</strong> to just create the app in Intune. When you are ready, you can edit the Deployment and add the required Assignment types.</p>
</blockquote>

* On the <strong>Assignments</strong> tab, if you do not want to set up any Detection Rules, you can click <strong>Migrate</strong>. If you do want to set up Detection Rules, you should click next to proceed to the <strong>Detection Rules</strong> tab.
* On the <strong>Detection Rules</strong> tab, you can either continue with the <strong>Use Custom</strong> option, i.e. what we detected in ConfigMgr, or select the <strong>Patch My PC Default (Recommended)</strong> option instead and let us use our recommended settings.

When you click <strong>Migrate</strong>, the <strong>Success – Deployment Created, Migration Pending</strong> notification is shown.

![“Migrate, the Success – Deployment Created, Migration Pending” notification](/_images/image-(7).png "“Migrate, the Success – Deployment Created, Migration Pending” notification")

The <strong>Status</strong> field also updates to show <strong>In Progress</strong> as the deployment is being created, with any required content being zipped (such as the primary installer file and any extra files) and sent to Azure Blob Storage.

You can also monitor the progress of the deployment by clicking the <strong>Deployments</strong> node and watching for the <strong>Status</strong> of the deployment to change to <strong>Success</strong>.

![Monitoring the status of the deployment](/_images/image-(8).png "Monitoring the status of the deployment")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>To see the migrated app in Intune, within the Microsoft Intune admin center navigate to:</p>
<p><strong>Home > Apps | Windows >Windows | Windows Apps ><</strong>_<strong>app\_name</strong>_<strong>></strong></p>
<p>![Migrated app in Intune](/_images/image-(9).png>)</p>
</blockquote>