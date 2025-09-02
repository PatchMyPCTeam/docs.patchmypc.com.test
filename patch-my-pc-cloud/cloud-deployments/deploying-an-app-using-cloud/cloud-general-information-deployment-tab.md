# Cloud "General Information" Deployment tab

_Applies to: Patch My PC Cloud_

The **General Information** tab of the Patch My PC (PMPC) Cloud deployment wizard allows you to configure various general settings (explained below) for how you want the app to be deployed.

{% hint style="info" %}
**Note**

If an app has multiple variants with different version numbers, besides the version you will see a yellow triangle with an exclamation mark in it  warning you of this.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (2383).png" alt="&#x22;General Information&#x22; tab" width="563"><figcaption></figcaption></figure>

<table><thead><tr><th width="140">Section</th><th>Description</th></tr></thead><tbody><tr><td>Apply Template</td><td>Allows you to apply a <a href="../use-a-template-in-cloud-deployments.md">Template</a> of pre-configured settings to this deployment.</td></tr><tr><td>Connection</td><td>Shows the type of connection. Currently, we only support connections to Intune.</td></tr><tr><td>Display Name</td><td>The unique name for this deployment. This is also the name of the app as it will appear on the target devices.<br><br><mark style="color:blue;"><strong>NOTE</strong></mark><br>This <strong>Display Name</strong> has to be unique per operating system. For example, you can have two deployments for the same app if one is targeted to macOS and the other Windows. You cannot have two deployments with the same name if they are both targeted to either macOS or Windows.</td></tr><tr><td>Language</td><td><p>Multiple language entries will be present if the vendor offers separate installers for that language. For example, an EXE installer for en-US, de-DE, etc. The majority of installers are multi-language (one installer, multiple languages), and the software can be configured in different languages by:</p><ul><li>Specifying additional installation parameters</li><li>Configuring .config or .xml files</li><li>Setting registry values.</li></ul><p>In such cases, it is the vendor that determines the level of support and the behavior.</p></td></tr><tr><td>Architecture</td><td><p>The architecture of the installer to be deployed:</p><ul><li>64-bit installers can only be installed on 64-bit devices</li><li>32-bit installers can typically be installed on either 32-bit or 64-bit devices. </li><li>Unspecified installers typically contain install logic for both architectures.</li></ul></td></tr><tr><td>Install Context</td><td><p>The context in which to install the application:</p><ul><li><strong>System –</strong> Available to all users.</li><li><strong>User –</strong> Available only to the specific user.</li></ul></td></tr><tr><td>Installer Type</td><td><p>The available installer types you can choose from to install this app:<br><br><strong>Windows Installer Types</strong></p><ul><li>.exe</li></ul><ul><li>.msi</li></ul><ul><li>.msp</li></ul><p><strong>Note</strong><br>If the <strong>.msi</strong> option is greyed out, it's probably because this is a <a href="../../binary-free-apps/binary-free-apps-overview.md">Binary Free</a> app, i.e. you need to manually download the installer from the vendor and create it in PMPC Cloud as a <a href="../../binary-free-apps/deploy-a-binary-free-app.md">Binary Free App</a> (the "<strong>Upload the required installer via 'Manage Files' to enable selection of this variant</strong>" message indicates this).</p><p><br>Also, if this is a macOS app, we currently support the following installer types:</p><ul><li>.dmg</li><li>.pkg</li></ul></td></tr></tbody></table>

***

Once you have finished configuring the relevant options, click **Next** to move to the [Configurations ](cloud-configurations-deployment-tab/)tab.

<figure><img src="../../../.gitbook/assets/image (2384).png" alt="clicking &#x22;Next&#x22; to move to the &#x22;Configurations&#x22; page" width="563"><figcaption></figcaption></figure>
