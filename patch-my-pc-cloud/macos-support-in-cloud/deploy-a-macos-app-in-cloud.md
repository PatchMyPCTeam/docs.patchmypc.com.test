# Deploy a macOS app in Cloud

_Applies to: Patch My PC Cloud_

Using Patch My PC (PMPC) Cloud, users can deploy **.DMG** or **.PKG** apps to Intune-managed devices running macOS.

<blockquote class="wp-block-quote is-note">
<p>We currently do not support deploying PMPC Cloud Custom Apps to macOS devices.</p>
<p>See [Deploying LOB app specifics](deploy-a-macos-app-in-cloud.md#deploying-lob-app-specifics) below for more details on deploying this type of app with PMPC Cloud and <a href="https://learn.microsoft.com/en-us/mem/intune/apps/lob-apps-macos">How to add macOS line-of-business (LOB) apps to Microsoft Intune</a> for more details on deploying this type of app with Microsoft Intune.</p>
</blockquote>

To deploy a macOS app using Patch My PC (PMPC) Cloud:

1.  Locate the required app on the App Catalog page.\


    ![Locating the app to be deployed](/_images/image-(2285).png "Locating the app to be deployed")

<blockquote class="wp-block-quote is-tip">
<p>Use the Search field and filters to help you locate the app.</p>
</blockquote>

2.  Click the relevant app.\


    ![Clicking the relevant app](/_images/image-(2286).png "Clicking the relevant app")


3.  On the app’s properties page, click **Deploy** under the **macOS** section to start the Deployment Wizard.\


    ![Clicking "Deploy" under the "macOS" section](/_images/image-(291).png "Clicking “Deploy” under the “macOS” section")
4. Continue from [General Information](../cloud-deployments/deploying-an-app-using-cloud/cloud-general-information-deployment-tab.md) to configure the deployment as required.

<blockquote class="wp-block-quote is-note">
<p>Due to the differences between the way Intune handles Windows and macOS apps, not all options are available for macOS apps. As Microsoft improves macOS support in Intune, we will endeavor to support any such improvements in PMPC Cloud.</p>
<p>For now, the following key differences exist:</p>
<p>* **Installer Types** (**Genera**l tab) – macOS only supports **.dmg** and **.pkg** installers.</p>
<p>* **Architecture** (**General** tab) – macOS supports the **Universal** type, which works on all architectures of macOS devices.</p>
<p>* **Installer Scripts** (**Configurations** tab) – For macOS, this option is only available if the installer type is **.pkg**.</p>
<p>* **Assignment Types** (**Assignments** tab) –  The **Add Update Only** and **Add Uninstall** assignment types are unavailable if the **Installer Type** is **.dmg** or **.pkg**. However, if the **InstallAsManaged** property has been enabled in the **.pkg**, the **Add Uninstall** assignment type will be available.\</p>
<p>\</p>
<p>Once you've added an Assignment, the following options are unavailable:</p>
<p>* Filter</p>
<p>* Availability / Deadline</p>
<p>*</p>
<p>Notifications</p>
<p>*</p>
<p>Content Download</p>
</blockquote>

<blockquote class="wp-block-quote is-tip">
<p>Once a macOS deployment has been completed successfully, you’ll can see it under **Apps | Monitor | macOS | macOS apps** in the Microsoft Intune admin center.</p>
<p>![Successful deployment visible in the Microsoft Intune admin center](/_images/image-(2289 "Successful deployment visible in the Microsoft Intune admin center").png>)</p>
</blockquote>

### Deploying LOB app specifics

When deploying _Line-of-Business_ (LOB) apps (also known as Custom or in-house apps), using PMPC Cloud, the following apply:

* We don’t visually identify LOB apps specifically in our App Catalog.
* When deploying a LOB app, the following additional options become available in the Deployment Wizard (even if the app uses a **.pkg** installer):
  * **Configurations** tab – The **Install scripts** section, which allows you to add a pre or post-install script.
  * **Assignments** tab - You can add an **Add Uninstall** assignment type.

<blockquote class="wp-block-quote is-important">
<p>Adding either a pre or post-install script results in the **Add Uninstall** assignment type being unavailable, as this combination is unsupported (hovering your mouse over the **Add Uninstall** assignment tells you that **Adding a script will disable uninstall assignments for this deployment**).</p>
<p>Likewise, if you add an **Add Uninstall** assignment and then click the **Configurations** page, the option to add either a pre or post-install script is greyed out (hovering your mouse over the **Add** button tells you **Uninstall Assignments disabled as you have added a pre/post-install script.**</p>
<p>!["Uninstall Assignments disabled as you have added a pre/post-install script."](/_images/image-(2395 "\"Uninstall Assignments disabled as you have added a pre/post-install script.\"").png>)</p>
<p>See [Supported Assignment Types & Settings for macOS Deployments](supported-assignment-types-and-settings-for-cloud-macos-deployments.md) for more details.</p>
</blockquote>