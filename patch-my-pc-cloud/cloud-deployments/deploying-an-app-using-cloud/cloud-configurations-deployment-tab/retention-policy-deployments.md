# Retention Policy (Deployments)

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Using the **Retention Policy** tool is optional and is not supported by the MSP App Sets feature.</p>
</blockquote>

The **Retention Policy** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to determine how many versions of an app (both Windows and macOS) you want to keep. If deploying a later version of an app causes issues, you can redeploy an older version.

By default, PMPC only retains the latest version of an app in your environment. Configuring a Retention Policy allows you to keep the current version, plus the number of configured versions as set by the Retention Policy.

For example, setting a Retention Policy of 1 for Google Chrome would mean you always have _n-1_ versions of Chrome, the latest and the previous version, until a newer version is deployed.

To configure a PMPC Cloud deployment to use a Retention Policy:

1. Click the **Retention Policy** tool.

![Clicking the "Retention Policy" tool](/_images/image-(99Retention-Policy "Clicking the \"Retention Policy\" tool").png "Clicking the “Retention Policy” tool")

2. Scroll down to the **Retention Policy** section.

![Scrolling down to the "Retention Policy" section.](/_images/image-(100Retention-Policy." "Scrolling down to the \"Retention Policy\" section.").png "Scrolling down to the “Retention Policy” section.")

3. In the **Versions to Retain** box, either type the required number or use the controls to configure the number of versions of this app you wish to retain in your environment.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>The default value of **0** means only the most recent version of the app is retained. You can retain up to ten versions of an app.</p>
</blockquote>

![Configuring the number of versions of this app to retain using the "Versions to Retain" box](/_images/image-(61Versions-to-Retain "Configuring the number of versions of this app to retain using the \"Versions to Retain\" box").png "Configuring the number of versions of this app to retain using the “Versions to Retain” box")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>See [Check App Version Retention](../../../cloud-reference/intune-reference/check-app-version-retention-in-intune.md) for details on how to check within Intune that the correct number of versions of an app are being retained as defined in your Retention Policy.</p>
</blockquote>

4. If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab. Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

![Clicking "Next" to move to the "Assignments" tab](/_images/image-(102Next "Clicking \"Next\" to move to the \"Assignments\" tab").png "Clicking “Next” to move to the “Assignments” tab")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Other important points about App Version Retention:</p>
<p>* Modifying the **Versions to Retain** setting is supported. The next time the [Sync Schedule](../../../cloud-administration/manage-the-sync-schedule-in-cloud.md) runs (or you manually [update an app](../../manage-updates-in-cloud/)), the changes will be applied to the deployment.</p>
<p>* Deleting a deployment or disconnecting [Intune ](../../../cloud-administration/manage-your-environments-in-cloud/manage-cloud-intune-tenants.md#deleting-an-intune-tenant-connection)will delete the latest and all old unassigned versions of all of your deployments.</p>
<p>* Modifying an existing deployment with a Retention Policy configured will only affect the current version, not all previous versions. For example, if you edit a deployment and add an extra file, the file is only added to the latest version, not all previous versions.</p>
<p>* You should avoid deleting versions of apps manually using the Intune admin center. Inadvertently deleting a previous version from Intune will not break the Retention Policy for the deployment. When a newer version is deployed, we will delete the relevant previous version(s) accordingly to keep everything in sync.</p>
</blockquote>