# Deploy the same App with Cloud using multiple configurations

_Applies to: Patch My PC Cloud_

You can deploy the same app with different configurations using Patch My PC (PMPC) Cloud.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>For this to work, you must use a different <strong>Display Name</strong> for the deployment. If you don't, you will receive the [deployment with the same name already exists](../cloud-troubleshooting/troubleshooting-cloud-deployments/a-deployment-with-the-same-name-less-than-deployment_name-greater-than-already-exists-error-when-dep.md) error.</p>
</blockquote>

To deploy the same app with a different configuration:

1. Sign in to the portal at [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2. Locate the required app on the <strong>App Catalog</strong> page.

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>Use the <strong>Search</strong> field to help you locate the app.</p>
</blockquote>

![“App Catalog” page](/_images/image-(741).png "“App Catalog” page")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>The green cloud icon beside the version number tells you this software has already been deployed using PMPC Cloud.</p>
</blockquote>

3. Click the app to open its properties, then click <strong>Deploy</strong> to start the Deployment Wizard.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See the [Deploy an App](deploying-an-app-using-cloud/) for more details. You can also apply a deployment template to this deployment by clicking <strong>Apply Template</strong> and following the [Use a Template in Deployments](use-a-template-in-cloud-deployments.md) process.</p>
</blockquote>

![Clicking &#x22;Deploy&#x22; on the App&#x27;s properties page](/_images/image-(487).png "Clicking &#x22;Deploy&#x22; on the App&#x27;s properties page")

4. On the G<strong>eneral Information</strong> tab, in the <strong>Display Name</strong> field, enter a unique name for this deployment, then click <strong>Next</strong>.

![&#x22;General Information&#x22; page](/_images/image-(2615).png "&#x22;General Information&#x22; page")

5. On the <strong>Configurations</strong> tab, configure the settings to add any required scripts or additional installation parameters, then click <strong>Next</strong>.

![&#x22;Configurations&#x22; tab](/_images/image-(2616).png "&#x22;Configurations&#x22; tab")

6. On the <strong>Assignments</strong> tab, click <strong>Add Assignment</strong>, then select the assignment type you want to add for this deployment.

![Clicking &#x22;Add Assignment&#x22;, then selecting the assignment type you want to add for this deployment](/_images/image-(2617).png "Clicking &#x22;Add Assignment&#x22;, then selecting the assignment type you want to add for this deployment")

7. On the <strong>Add <</strong>_<strong>assignment\_type</strong>_<strong>> Assignment</strong> page, select the relevant options, then click <strong>Save</strong>.

![](/_images/image-(2618).png "")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you add an available assignment, as shown below, we recommend selecting the same options in the <strong>Add update only app for</strong> section. Doing this will automatically make the current version of the app and any updates (current or future) available.\</p>
</blockquote>

The <strong>Assignments</strong> page updates to show the newly created deployment.

![New assignment shown on the “Assignments” page](/_images/image-(2619).png "New assignment shown on the “Assignments” page")

8. Configure the settings for deployment, if required.

![Configure any required settings](/_images/image-(2620).png "Configure any required settings")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>We automatically configure these settings based on our experience and best practices, but you can modify certain settings if necessary.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can click <strong>Deploy</strong> on this page if you don’t want to add additional assignments or see the <strong>Overview</strong> page, which allows you to double-check the settings you’ve configured for this deployment.</p>
</blockquote>

9. Add any additional assignments for this deployment by clicking <strong>Add Assignment</strong> and repeating Steps 6 to 8, then click <strong>Next</strong>.

![Adding  any additional assignments for this deployment by clicking &#x22;Add Assignment&#x22;](/_images/image-(2621).png "Adding  any additional assignments for this deployment by clicking &#x22;Add Assignment&#x22;")

10. Review the deployment summary shown on the <strong>Summary</strong> page.\
    \
    If you are happy, click <strong>Deploy</strong>.

![Clicking &#x22;Deploy&#x22;](/_images/image-(2622).png "Clicking &#x22;Deploy&#x22;")

If you need to change something, click <strong>< Prev</strong> to backtrack through the Deployment Wizard to the relevant setting. Make the change, then step back through the wizard to this page. If everything is now correct, click <strong>Deploy</strong>.

The <strong>Deployments</strong> page is displayed along with the <strong>Success - Created&#x20;</strong>_<strong>\<deployment\_name></strong>_ notification.

![](/_images/image-(2624).png "")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>By default, the installation logs for an app will be created in the following folder regardless of the installer file type:</p>
<p>`%ProgramData%\PatchMyPCInstallLogs`</p>
<p>The only exception is for EXE files, where the specified value for the <strong>loggingSwitch</strong> variable will be used if it is not null or empty.</p>
</blockquote>