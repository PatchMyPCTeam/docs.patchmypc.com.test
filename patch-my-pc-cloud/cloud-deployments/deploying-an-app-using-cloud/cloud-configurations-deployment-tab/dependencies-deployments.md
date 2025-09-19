# Dependencies (Deployments)

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Using the **Depencies** tool is optional.</p>
</blockquote>

The **Dependencies** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to create dependencies within a deployment, whereby the app being deployed requires one or more other apps to have already been installed on the targeted resource before it can be deployed.

If the required app(s) (known as the _parent_) has not already been installed on the device, they will automatically be installed before the app that is being deployed (known as the _child app_) is installed.

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>Before you can create an App Dependency in a PMPC Cloud deployment, the deployment for the parent app(s) must:</p>
<p>* exist already</p>
<p>* have been deployed successfully</p>
<p>Also, apps that have not been successfully deployed (such as those with a status of **Failed**, **Retrying**, **Processing**, etc.) cannot be used to create an app dependency, nor can apps with **Uninstall** or **Update Only** assignments.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Like Intune, we do not support circular dependencies (i.e. App A has a dependency on App B, and App B has a dependency on App A).</p>
<p>As per Intune, you can create a maximum of 100 dependencies, which includes the dependencies of any included dependencies, as well as the app itself. See <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-win32-add#step-5-dependencies">Step 5: Dependencies</a> of <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-win32-add">Add, assign, and monitor a Win32 app in Microsoft Intune</a> for more information.</p>
</blockquote>

!["Dependencies" tool](/_images/image-(88Dependencies "\"Dependencies\" tool").png "“Dependencies” tool")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>The parent app must have been deployed successfully before you can create a dependency between apps.</p>
</blockquote>

To add a dependency:

1. Click the **Dependencies** tool.

![Clicking the "Dependencies" tool](/_images/image-(89Dependencies "Clicking the \"Dependencies\" tool").png "Clicking the &#x22;Dependencies&#x22; tool")

2. From the **Add Dependencies** field, either:
   1. Start typing the name of the relevant app that this app depends on already being successfully installed on the target device.
   2. Click the dropdown and select the relevant app that this app depends on already being successfully installed on the target device.

![Selecting the relevant app that this app depends on already being successfully installed on the target device](/_images/image-(90 "Selecting the relevant app that this app depends on already being successfully installed on the target device").png "Selecting the relevant app that this app depends on already being successfully installed on the target device")

The selected app appears under the **Parent Deployment** section.

![Selected app appearing under the "Parent Deployment" section](/_images/image-(91Parent-Deployment "Selected app appearing under the \"Parent Deployment\" section").png "Selected app appearing under the “Parent Deployment” section")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Click the trashcan beside the relevant app under the **Parent Deployment** section to delete a dependency.</p>
</blockquote>

3. Repeat Step 2. to add any additional dependencies.

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>Once a dependency has been configured, you can view it as part of the app’s properties in the Microsoft Intune admin center.</p>
<p>![Viewing dependencies for an app in the Microsoft Intune admin center](/_images/image-(339 "Viewing dependencies for an app in the Microsoft Intune admin center").png>)</p>
<p>For more information, see <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-win32-add#step-5-dependencies">Step 5: Dependencies</a> of <a href="https://learn.microsoft.com/en-us/mem/intune/apps/apps-win32-add">Add, assign, and monitor a Win32 app in Microsoft Intune</a>.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If a dependency is set up in the Intune admin center between an app managed by PMPC Cloud and an app managed directly in Intune, we will always copy-forward any dependencies from the PMPC Cloud app whenever we update the PMPC Cloud app.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Warnings**</p>
<p>If we encounter any problems with app dependencies, we display a yellow exclamation mark (“**!**”) warning. Hovering over this will display more information.</p>
<p>![](/_images/image-(334).png)</p>
<p>We typically generate warnings in the following scenarios:</p>
<p>* If a dependency fails to be created. In this case, a warning is shown on the impacted child app(s) at the deployment level.</p>
<p>* If a dependency fails to be carried forward. In this case, a warning is shown on the impacted child app(s) at the deployment level.</p>
<p>* When multiple parent dependencies exist, any warnings will specify which particular dependency failed to be created to help you troubleshoot the issue.</p>
<p>If an entire deployment fails before the dependencies stage is reached, no warnings are shown, as we only show warnings for successful deployments.</p>
</blockquote>

4.  If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\


    Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

![Clicking "Next" to move to the "Assignments" page](/_images/image-(92Next "Clicking \"Next\" to move to the \"Assignments\" page").png "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page")