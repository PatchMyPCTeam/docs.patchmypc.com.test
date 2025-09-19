# Deploying an App using Cloud

_Applies to: Patch My PC Cloud_

Patch My PC (PMPC) Cloud can be used to deploy apps using Microsoft Intune.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>See [Deploying the same App with multiple configurations](../deploy-the-same-app-with-cloud-using-multiple-configurations.md) for details on re-using a successfully deployed app for different configurations.</p>
<p>See [Create a Deployment with No Assignments](../create-a-cloud-deployment-without-assignments.md) for details on how to create a deployment without assignments.</p>
</blockquote>

Deploying an app with PMPC Cloud involves configuring:

* [General Information](cloud-general-information-deployment-tab.md)
* [Various Configurations](cloud-configurations-deployment-tab/) (optional)
  * [Scripts](cloud-configurations-deployment-tab/cloud-scripts-deployment-tool/) (optional)
  * [Installation Parameters](cloud-configurations-deployment-tab/install-parameters-deployments.md) (optional)
  * [Dependencies](cloud-configurations-deployment-tab/dependencies-deployments.md) (optional)
  * [Role Scope Tags](cloud-configurations-deployment-tab/role-scope-tags-optional.md) (optional)
  * [Extra Files](cloud-configurations-deployment-tab/extra-files-deployments.md) (optional)
  * [Categories](cloud-configurations-deployment-tab/categories-deployments.md) (optional)
  * [ESP Profiles](cloud-configurations-deployment-tab/esp-profiles-deployments.md) (optional)
* [Assignments](cloud-assignments-deployment-tab.md)
* [Summary](cloud-summary-deployment-tab.md) (optional but recommended)

### Deploying an App

To deploy an app using PMPC Cloud:

1. Sign in to the portal at [https://portal.patchmypc.com/](https://portal.patchmypc.com/)
2. Locate the required application on the **App Catalog** page.

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>Use the **Search** field to help you locate the app.</p>
</blockquote>

!["App Catalog" page](/_images/image-(193 "\"App Catalog\" page").png "“App Catalog” page")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If an app (for example, the Windows version of Slack) has multiple versions available for different variants/installer types, the App Catalog shows the total number of available versions. If you hover your mouse over this, you can see the list of variants grouped accordingly. Only that version will be displayed if a single version is available for all variants.</p>
<p>![Total number of available variants](/_images/image-(2471 "Total number of available variants").png>)</p>
</blockquote>

3.  Click the app to open its properties.\


    ![Application's "Properties" page](/_images/image-(194 "Application's \"Properties\" page").png "Application’s “Properties” page")


4. Click **Deploy** to start the Deployment Wizard.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If the app you are deploying is also supported for macOS, you will see a separate **Deploy** option for **macOS**  and you should follow the [Deploy a macOS app](../../macos-support-in-cloud/deploy-a-macos-app-in-cloud.md) process.</p>
<p>Also, if the app you are deploying is already published by our on-premises Publisher, you will see the **This app is already deployed** warning dialog stating that deploying the same app through both Publisher and PMPC Cloud can cause potential issues if there are differences between the deployment configurations. We therefore strongly recommend you only deploy an app through either Publisher PMPC Cloud to avoid such issues.</p>
</blockquote>

![Click "Deploy" to start the Deployment Wizard](/_images/image-(195 "Click \"Deploy\" to start the Deployment Wizard").png "Click &#x22;Deploy&#x22; to start the Deployment Wizard")

The [General Information](cloud-general-information-deployment-tab.md) tab is displayed, which needs to be completed.