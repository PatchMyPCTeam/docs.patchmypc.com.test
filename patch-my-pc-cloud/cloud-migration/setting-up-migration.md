# Setting up Migration

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.</p>
<p>Please do not share links to these docs with others outside of the Private Preview.</p>
<p>Once this feature is released, it will be announced and this banner removed.</p>
</blockquote>

Before you can perform a migration using the Patch My PC (PMPC) Cloud _Migration_ feature, you need to ensure that your On-Premises Publisher (Publisher) is connected to the same PMPC Cloud Company that you plan to migrate the objects to.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See [Add a Connection](../cloud-administration/manage-cloud-connections/add-a-connection.md) for further details.</p>
</blockquote>

You also need to ensure that the <strong>Enable Application Migration</strong> checkbox on the <strong>Cloud</strong> tab is checked.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you do not see the <strong>Enable Application Migration</strong> checkbox on the <strong>Cloud</strong> tab, ensure you are running the required version of Publisher as detailed in [Migration Requirements](migration-requirements.md).</p>
</blockquote>

![“Enable Application Migration” checkbox is checked on the “Cloud” tab](/_images/image-(2713).png "“Enable Application Migration” checkbox is checked on the “Cloud” tab")

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>If you click <strong>Disconnect</strong> on the <strong>Cloud</strong> tab of the <strong>Publisher</strong>, all of the data for the Migration feature will be deleted from your PMPC Cloud company. You should avoid doing this until you have completed the migration of everything you need to migrate from ConfigMgr to PMPC Cloud.</p>
</blockquote>

Next, sign in to your PMPC Cloud company and verify that the <strong>Migration</strong> node is visible.

![Verifying the “Migration” node is visible in the PMPC Cloud portal](/_images/image-(2714).png "Verifying the “Migration” node is visible in the PMPC Cloud portal")

When you navigate to <strong>Migration</strong>, the <strong>Migration</strong> page is displayed, showing a list of the ConfigMgr applications that have been detected with the following information.

<table><thead><tr><th width="137" valign="top">Field</th><th>Description</th></tr></thead><tbody><tr><td valign="top">Match Type</td><td><p>The result of our attempt to match the ConfigMgr application to an app in our App Catalog, which will be one of the following:</p><p></p><p><strong>PMPC App –</strong> We have successfully matched the ConfigMgr application to a version in our catalog. These apps can be deployed into Intune as a PMPC App and kept up to date by us for you.<br><br><strong>Custom App –</strong> We have been unable to successfully match the ConfigMgr application to a version in our catalog, but we can still help you migrate it to Intune.<br><br><strong>Not Supported –</strong> We cannot currently migrate the ConfigMgr application, such as PSADT, or an app we’ve published from our Publisher to ConfigMgr, where it doesn’t make sense to migrate it, as you can just deploy it straight from our catalog to Intune using PMPC Cloud.<br><br><mark style="color:green;"><strong>TIP:</strong></mark><br>You can hover over the “<strong>(i)</strong>” for an unsupported match type to see why it is unsupported for migration.</p></td></tr><tr><td valign="top">Matched App</td><td>The name of the app we have matched the ConfigMgr application to in our catalog.</td></tr><tr><td valign="top">Status</td><td><p>The migration status of the ConfigMgr application, which will be one of the following:<br><br><strong>Not Started –</strong> The migration process has not been started.</p><p><strong>Pending –</strong> The migration process has been initiated.</p><p><strong>In Progress –</strong> The migration is in progress.</p><p><strong>Migrated –</strong> The application has been successfully migrated to PMPC Cloud.</p></td></tr><tr><td valign="top">Info</td><td>If there is further information/warnings about this application that we want you to review (such as we’ve detected a setting in the ConfigMgr application we cannot migrate), a warning triangle is displayed in the <strong>Info</strong> column.<br><br>The triangle includes a number, which is the number of warnings. If you hover your mouse over the triangle, you will see a summary, and if you click the triangle, it will open the properties of the application and display the triangle beside the items we are warning you about.<br><br>Clicking the triangle will show you more details that you should review before continuing to migrate the application.</td></tr></tbody></table>

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>The last column displays the <strong>Migrate</strong> button, which is what you actually click to migrate the application. The <strong>Migrate</strong> button will be unavailable if:</p>
<p>* The application cannot be migrated or has already been migrated to PMPC Cloud.</p>
<p>* You do not have the correct license for your PMPC Cloud Company.</p>
</blockquote>

By default the Publisher polls the ConfigMgr Site Database every 60 minutes for changes.

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>The following log files can be used for more information and for troubleshooting the migration feature:</p>
<p>`"%ProgramFiles%\Patch My PC\Patch My PC Publishing Service\Logs\PatchMyPC-AppMigrationService.log”`&#x20;</p>
<p>`"%ProgramFiles%\Patch My PC\Patch My PC Publishing Service\Logs\PatchMyPC-CloudFileUploadBackgroundService.log”`</p>
<p>`"%ProgramFiles%\Patch My PC\Patch My PC Publishing Service\PatchMyPC.log”`</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Note:</strong></p>
<p>For new installations of Patch My PC Publisher, the <strong>PatchMyPC.log</strong> file will exist in the following folder:</p>
<p>`"%ProgramFiles%\Patch My PC\Patch My PC Publishing Service\Logs"`</p>
</blockquote>