# Cloud "Scripts" Deployment Tool

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Using the **Scripts** tool is optional.</p>
</blockquote>

The **Scripts** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to configure settings for install and uninstall scripts.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>* Scripts will be run in the same context as the application.</p>
<p>* Each install script is limited to 1 MB per script, with a total size limit of 4 MB for all scripts.</p>
<p>* There is a limit of 50,000 characters per script.</p>
<p>We currently support the following script types:</p>
<p>* .BAT</p>
<p>* .CMD</p>
<p>* .PS1</p>
<p>* .VBS</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>Currently, scripts containing `"${env:ProgramFiles(x86)}"` or `"${env:ProgramFiles}"` cannot be uploaded as Cloudflare is falsely identifying them as a false positive related to Log4j exploits. We are actively working with them to resolve this, but as this is outside our control, we cannot provide an estimated resolution time.</p>
<p>To work around this issue, see the [Resolution](../../../../cloud-troubleshooting/troubleshooting-cloud-deployments/typeerror-failed-to-fetch-error-when-trying-to-upload-a-pre-or-post-script-in-cloud.md#resolution) section of ["TypeError: Failed to fetch" error when trying to upload  a Pre or Post Script](../../../../cloud-troubleshooting/troubleshooting-cloud-deployments/typeerror-failed-to-fetch-error-when-trying-to-upload-a-pre-or-post-script-in-cloud.md).</p>
</blockquote>

To add a script:

1. Click the **Scripts** tab to expose the configurable settings.

![Clicking the "Scripts" tab to expose the configurable settings](/_images/image-(2603 'Clicking the "Scripts" tab to expose the configurable settings').png "Clicking the &#x22;Scripts&#x22; tab to expose the configurable settings")

2. Click **Add** beside the relevant script option to add a script, then configure the required settings as per the relevant articles:

* [Pre-Install Script](cloud-pre-install-scripts.md) - a script that can be run before the installer runs.
* [Post-Install Script](cloud-post-install-scripts.md) - a script that can be run after the installer runs.
* [Pre-Uninstall Script](cloud-pre-uninstall-scripts.md) - a script that can be run before the uninstaller runs.
* [Post-Uninstall Script](cloud-post-uninstall-script.md) - a script that can be run after the uninstaller runs.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If you upload [Extra Files](../extra-files-deployments.md) as part of your Patch My PC (PMPC) Cloud Deployment, you can reference those files in any of the [Scripts](./) in the same deployment by building a path relative to the script's current location. See [Referencing Extra Files in Scripts](../../../cloud-deployments-reference/referencing-extra-files-in-scripts.md) for more information.</p>
</blockquote>

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.