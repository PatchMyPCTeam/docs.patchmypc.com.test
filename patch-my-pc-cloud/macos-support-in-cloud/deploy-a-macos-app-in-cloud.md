# Deploy a macOS app in Cloud

_Applies to: Patch My PC Cloud_

Using Patch My PC (PMPC) Cloud, users can deploy <strong>.DMG</strong> or <strong>.PKG</strong> apps to Intune-managed devices running macOS.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>We currently do not support deploying PMPC Cloud Custom Apps to macOS devices.</p>
<p>See [Deploying LOB app specifics](deploy-a-macos-app-in-cloud.md#deploying-lob-app-specifics) below for more details on deploying this type of app with PMPC Cloud and <a href="https://learn.microsoft.com/en-us/mem/intune/apps/lob-apps-macos">How to add macOS line-of-business (LOB) apps to Microsoft Intune</a> for more details on deploying this type of app with Microsoft Intune.</p>
</blockquote>

To deploy a macOS app using Patch My PC (PMPC) Cloud:

1.  Locate the required app on the App Catalog page.\


    ![Locating the app to be deployed](/_images/image-(2285).png "Locating the app to be deployed")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>Use the Search field and filters to help you locate the app.</p>
</blockquote>

2.  Click the relevant app.\


    ![Clicking the relevant app](/_images/image-(2286).png "Clicking the relevant app")


3.  On the app’s properties page, click <strong>Deploy</strong> under the <strong>macOS</strong> section to start the Deployment Wizard.\


    ![Clicking “Deploy” under the “macOS” section](/_images/image-(291).png "Clicking “Deploy” under the “macOS” section")
4. Continue from [General Information](../cloud-deployments/deploying-an-app-using-cloud/cloud-general-information-deployment-tab.md) to configure the deployment as required.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Due to the differences between the way Intune handles Windows and macOS apps, not all options are available for macOS apps. As Microsoft improves macOS support in Intune, we will endeavor to support any such improvements in PMPC Cloud.</p>
<p>For now, the following key differences exist:</p>
<p>* <strong>Installer Types</strong> (<strong>Genera</strong>l tab) – macOS only supports <strong>.dmg</strong> and <strong>.pkg</strong> installers.</p>
<p>* <strong>Architecture</strong> (<strong>General</strong> tab) – macOS supports the <strong>Universal</strong> type, which works on all architectures of macOS devices.</p>
<p>* <strong>Installer Scripts</strong> (<strong>Configurations</strong> tab) – For macOS, this option is only available if the installer type is <strong>.pkg</strong>.</p>
<p>* <strong>Assignment Types</strong> (<strong>Assignments</strong> tab) –  The <strong>Add Update Only</strong> and <strong>Add Uninstall</strong> assignment types are unavailable if the <strong>Installer Type</strong> is <strong>.dmg</strong> or <strong>.pkg</strong>. However, if the <strong>InstallAsManaged</strong> property has been enabled in the <strong>.pkg</strong>, the <strong>Add Uninstall</strong> assignment type will be available.\</p>
<p>\</p>
<p>Once you've added an Assignment, the following options are unavailable:</p>
<p>* Filter</p>
<p>* Availability / Deadline</p>
<p>*</p>
<p>Notifications</p>
<p>*</p>
<p>Content Download</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>Once a macOS deployment has been completed successfully, you’ll can see it under <strong>Apps | Monitor | macOS | macOS apps</strong> in the Microsoft Intune admin center.</p>
<p>![Successful deployment visible in the Microsoft Intune admin center](/_images/image-(2289).png>)</p>
</blockquote>

### Deploying LOB app specifics

When deploying _Line-of-Business_ (LOB) apps (also known as Custom or in-house apps), using PMPC Cloud, the following apply:

* We don’t visually identify LOB apps specifically in our App Catalog.
* When deploying a LOB app, the following additional options become available in the Deployment Wizard (even if the app uses a <strong>.pkg</strong> installer):
  * <strong>Configurations</strong> tab – The <strong>Install scripts</strong> section, which allows you to add a pre or post-install script.
  * <strong>Assignments</strong> tab - You can add an <strong>Add Uninstall</strong> assignment type.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>Adding either a pre or post-install script results in the <strong>Add Uninstall</strong> assignment type being unavailable, as this combination is unsupported (hovering your mouse over the <strong>Add Uninstall</strong> assignment tells you that <strong>Adding a script will disable uninstall assignments for this deployment</strong>).</p>
<p>Likewise, if you add an <strong>Add Uninstall</strong> assignment and then click the <strong>Configurations</strong> page, the option to add either a pre or post-install script is greyed out (hovering your mouse over the <strong>Add</strong> button tells you <strong>Uninstall Assignments disabled as you have added a pre/post-install script.</strong></p>
<p>!["Uninstall Assignments disabled as you have added a pre/post-install script."](/_images/image-(2395).png>)</p>
<p>See [Supported Assignment Types & Settings for macOS Deployments](supported-assignment-types-and-settings-for-cloud-macos-deployments.md) for more details.</p>
</blockquote>