---
description: Test Cloud Release Notes here
---

# Cloud Release Notes

_Applies to: Patch My PC Cloud_

Details the production release history for Patch My PC (PMPC) Cloud, the most recent release being shown first.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>We aim to release new features, updates, and fixes at 12:00 CEST every Wednesday.</p>
<p>_Production Release_ means we have released that item to our Production environment i.e. customers can access it, although a specific feature maybe in one of the following three production states:\</p>
<p>* Private Preview, which is invitation only.</p>
<p>* Public Preview for which you will need to have [Preview Features enabled](cloud-administration/manage-your-cloud-company/enable-cloud-preview-features.md) in your company to access it.</p>
<p>* General Availability which is available to everyone.&#x20;</p>
<p>Please see the relevant docs for a feature for more information which will indicate the state of the feature.</p>
<p>You can also access this page from within the Cloud Portal by clicking the support button (!["support" button](/_images/image-(587).png>)) in the header area and selecting **Release Notes**.</p>
</blockquote>

### Week of August 6<sup>th</sup>, 2025

#### New Features

**Portal**

* **Customer Feedback –** Now, when you complete certain workflows for the first time, we give you the option of providing feedback on your experience.

**Managed Service Provider**

* **MSP Invites –** Managed Service Providers (MSPs) can now send invitation links to customers, allowing them to self-register and create their own companies within the system to be managed by the MSP

#### Fixes

**Portal**

* Resolved an issue where the ConfigMgr version of an app migrated to PMPC Cloud was deployed instead of the newer version in our App Catalog.

**Binary Free Apps**

* Resolved an issue where if a customer uploaded a newer version of an app, an older version was deployed.

### Week of July 30th,  2025

<details>

<summary>New Features</summary>

**Custom Apps**

* **Uninstall Arguments –** We’ve now added the ability for you to specify uninstall parameters for a Custom App.

**Intune Apps**

* **PMPC Scripts –** You can now see and disable any scripts we recommend for an app when you create a deployment.

**Managed Service Provider**

* **App Set Details –** You can now expand an App Set to see a list of the apps it contains and summary information for each app within the App Set.

</details>

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue with Microsoft SQL Server Management Studio 21, where assignments could only be created to either install or update this app. Now we support both.

**Custom Apps**

* Resolved an issue when creating a Custom App containing files with duplicate names but different extensions (e.g. **setup.exe** and **setup.zip**), generating a duplicate filename error.

**Intune Apps**

* Resolved an issue where attempting to add an assignment to an existing deployment failed with a **400 Bad Request** error.

**Managed Service Provider**

* Resolved an issue where adding a Child MSP company to an App Set containing a Custom App resulted in the app being stuck with a status of **In Progress** on the Child Company.
* Resolved an issue where adding a Child MSP company generated a **Bad request** error.

</details>

### Week of July 23rd,  2025

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue with some users receiving an “**An error occurred while processing your request**” when working with Branding.
* Resolved an issue with a **Limit** showing as red when it reached 99%, not 100%.
* Resolved an issue with a Discovery data failing to load, sometimes with a **TypeError: Failed to fetch** error.

**Custom Apps**

* Resolved an issue with Custom Apps getting stuck at stage of 3/3 after editing.

**Managed Service Provider**

* Resolved an issue with assignments not being shown correctly for MSP App Sets.

</details>

### Week of July 16th,  2025

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue where if the macOS trial banner was closed for one PMPC Cloud Company, if you logged into another company, the banner was also disabled.
* Resolved an issue with overlapping elements in the portal if a resolution lower than 1324 x 724px was used.
* Resolved an issue where if you had the **Remember my Selection** checkbox checked on the sign in page, then signed out, and selected a different company to sign into, you were signed into the company that was remembered, not the new one you selected to sign into.

**Custom Apps**

* Resolved an issue with an app’s icon not being displayed in a webhook when the deployment of a Custom App is updated via the Sync Schedule.

**Intune Apps**

* Resolved an issue when running Discovery for a new PMPC Cloud Company generating an error, which was resolved by clicking **Refresh**.
* Resolved an issue with the sorting of apps in Discovery not working correctly.
* Resolved an issue with excluding an Entra ID group from Branding now working.

**Managed Service Provider**

* Resolved an issue with adding a scripts and arguments to an MSP App Sets not being saved, as when you edited the App Set, the script and it’s arguments were missing.

</details>

### Week of July 9th,  2025

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue with **Company Recovery** being referred to as **Tenant Recovery** in the **Events** section.

</details>

### Week of July 2<sup>nd</sup>, 2025

<details>

<summary>New Features</summary>

**Portal**

* **New “Items per page” options –** We’ve added new values to the **Items per page** dropdown in the portal to allow you to choose to display more items per page in the portal.
* **Increased character limits –** We now support 2,048 characters in the following fields:
  * Install Parameters Additional Argument
  * Silent Install Parameters
  * Additional Silent Uninstall Parameters

**Custom Apps**

* **Version number replaced with “%” –** Now, when you add a Primary Install File that is an MSI, when populating the various properties, if we detect a version number in the **Apps & Features Name** field, we replace it with a "**%**".

</details>

<details>

<summary>Fixes</summary>

**Discovery**

* Resolved an issue where if a single Intune discovered app was mapped to two different products from our App Catalog, and one of them was managed and the other was unmanaged, one of them would appear under the **Managed** tab and the other would appear in the **Unmanaged** tab.\
  \
  Now, if one of them is managed and the other is unmanaged, the managed app is displayed in the **Managed** tab and the unmanaged app is hidden in the **Unmanaged** tab.\


**Custom Apps**

* Resolved an issue with a Custom Apps icon not being shown in a webhook when its deployment is updated via Sync Schedule.

**Managed Service Provider**

* Resolved an issue with an MSP not being able to unlink a child customer if their license had expired.

</details>

### Week of June 25<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

**Portal**

* **New "Usage" page –** We now show the usage limits for your PMPC Cloud company and your current usage to allow you to see when what you are using and when you are approaching a limit.
* **New tooltip for MSP deployments –** Now if you select the **.msp** installer when creating a deployment, we pop-up a warning that you will only be able add an Update Only assignment to this deployment and you should select the **.exe** installer if you want to use the other assignment types.
* **New default variant logic –** We’ve now replaced our existing language-only priority when creating a deployment with logic based on language, installation context, architecture, and installer type.

</details>

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue with Entra ID Groups not being sorted alphabetically in the portal when searching to add them to an assignment.

</details>

### Week of June 18<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

**Portal**

* **Granting PMPC Support Access –** We now provide a dropdown to allow you to choose the number of hours you want to grant our Support Team access to your PMPC Cloud company.

</details>

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue when sorting by operating system within Discovery not sorting correctly.

</details>

### Week of June 11<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

**Portal**

* **Improved UI for multi-versions –**&#x4E;ow if an app has multiple versions in the App Catalog that can be deployed, we indicate the number of versions available and allow you to select the relevant version you want to deploy from a dropdown on the app’s tile in the App Catalog.

**Intune Apps**

* **Ability to create an "Uninstall Branding" app –** You can now create this app which will create an Intune Win32 app, assigned as required with an uninstall intent, to remove any custom branding files from devices.

</details>

<details>

<summary>Fixes</summary>

**Intune Apps**

* Resolved an issue where a user could create a Windows Deployment Template with an ESP Profile and an Update Only Assignment. It should not be able to create such a combination.

</details>

### Week of June 4<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

**Binary Free Apps**

* **Improved validation –** Previously, you could upload one bitness of an app, but attempt to deploy a different bitness. It was only when you got to the end of the Deployment Wizard that we informed you of this mismatch.

</details>

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue with the text entered in the **Reason for Request** field when requesting access to a PMP Cloud Company not being populated in the portal.

</details>

### Week of May 28th, 2025

<details>

<summary>New Features</summary>

**Intune Apps**

* **Improved error handling for deployments when permissions are removed –** We have improved error handling for various deployment-related scenarios when permissions are either removed or amended when managing deployments.

</details>

<details>

<summary>Fixes</summary>

**Intune Apps**

* Resolved an issue with the incorrect error message being displayed when Company limits have been reached. We now show the correct error for the relevant cause.

</details>

### Week of May 21st, 2025

<details>

<summary>New Features</summary>

**Portal**

* **Templates –** You can now set the default type of Update Rings from within a Template.
* **Templates –** The **Tools** menu has been added to the **Configurations** page of templates to make it easier for you to navigate the various available sections.

</details>

<details>

<summary>Fixes</summary>

**Portal**

* Resolved an issue with the list of languages on the **Branding List** page showing the language that was configured first when it should be the default language.
* Resolved an issue where inserting a variable in the middle of text when defining naming standards actually inserted the variable at the end of the field and not at the chosen point in the text.
* Resolved an issue with **Exclude** filters configured on a deployment actually being applied as an **Include** filter.

**Intune Apps**

* Resolved an issue with Scope Tags manually added in Intune not being copied forward.

</details>

### Week of May 14th, 2025

<details>

<summary>New Features</summary>

Portal

* **Change to Self-Update template behavior –** Now when you create a Template, we check the **Disable Self-Update** option under the **Built-in Auto Updates** section by default (previously this was unchecked).
* **Change to Company Recovery option –** We’ve changed the language used for the **Company Recovery** section on the **Company** page to make it clearer.
* **New Update rings start time dropdown –** Previously, when creating a deployment, on the **Assignments** page, after clicking **Enable Update Rings** you had the choice of choosing to create either **Delayed** or **Immediate** rings. We’ve now moved the choices under a new **Update rings start time** dropdown, recommending **Delayed** and including tooltips to help guide you.

</details>

<details>

<summary>Fixes</summary>

**Custom Apps**

* Various bugs squashed to resolve issues with deployments getting stuck.
* Resolved an issue with the **Custom App Admin** not having access to the **App Catalog** page.

**Intune Apps**

* Resolved an issue with two deployments being created in Intune after a deployment with No Assignments is recreated.
* Various bugs squashed to resolve issues with deployments getting stuck.

</details>

### Week of May 7th, 2025

<details>

<summary>Fixes</summary>

**Intune Apps**

* Resolved an issue when adding extra files to an existing deployment (either through editing it or adding a new version) of those files missing from the deployment.
* Resolved an issue with config files larger than 28.6 MB failing to upload.

</details>

### Week of April 30th, 2025

<details>

<summary>New Features</summary>

#### Custom Apps

* **Improved error handling for macOS Custom Apps –** Previously, if you uploaded a **.pkg** or **.dmg** file as the primary installer file, we just showed an "**unsupported file**" notification. We now show the following notification:\
  "Custom Apps for macOS are not supported at this time. Vote and subscribe to [PMPC Cloud Portal - macOS Custom Apps](https://ideas.patchmypc.com/ideas/PATCHMYPC-I-6056) to receive updates on future development."

</details>

<details>

<summary>Fixes</summary>

#### Intune Apps

* Resolved an issue with Detection Rules when configuring the time for a **Date Modified** rule, where if a PM time was selected, it was actually saved as the corresponding AM time.

</details>

### Week of April 24th, 2025

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with notifications not being sent to the webhook when deployments with no assignments failed when being created or updated. This issue also affected Slack.
* Resolved an issue with failed deployments not being shown in the Updates Report.

</details>

### Week of April 16th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Recommend App Dependencies now shown –** When you now create an App Dependency, we automatically show a list of recommended apps (if relevant) that you should consider configuring as dependencies for the app being deployed.

</details>

<details>

<summary>Fixes</summary>

#### Managed Service Provider

* Resolved an issue with Naming Conventions when adding the “`&`” character as a prefix, it actually being added as "`&amp`”.        &#x20;

</details>

### Week of April 9th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Additional filters added to help when working with Deployments –** The filter list in the portal now includes new filters to only show which deployments are using Update Rings (enabled or disabled) as well as which deployments have updates paused or not.

</details>

### Week of April 2nd, 2025

<details>

<summary>New Features</summary>

#### Portal

* **UI improvements for Deployment Properties –** We’ve improved the UI when looking at the properties of a deployment so as not to truncate entries such as script names.

</details>

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with older versions of Apps and Updates not being removed even after the portal syncs and when the older version has made it through update rings.         &#x20;

#### Intune Apps

* Resolved an issue with email addresses being displayed incorrectly when a deployment has a large number of update rings.

</details>

### Week of March 25th, 2025

<details>

<summary>Fixes</summary>

#### Binary Free Apps

* Resolved an issue with users not being notified of a new version of an app being available if either the **Notify All Users in Company** or **Notify Specific Users** options are selected.

#### Custom Apps

* Resolved an issue when uploading extra files with the same name but in different folders, the UI didn’t process the folder structure and instead uploaded all of the files as independent files.

</details>

### Week of March 19th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Number of available versions now shown for apps in the App Catalog –** If multiple versions are available for different variants of the same app, App Cat will show the number of available versions. If you hover over the number, you can see the list of variants grouped accordingly. If only one version is available for all variants, only that version will be displayed.

#### Intune Apps

* **Native Detection Rules –** Patch My PC (PMPC) Cloud deployments now support Native Detection Rules.
* **Pre/Post Scripts now support Arguments –** Our Pre and Post Scripts now support additional arguments.

</details>

<details>

<summary>Fixes</summary>

#### Custom Apps

* Resolved an issue with the logo defined for a Custom App not appearing in Intune.

</details>

### Week of March 12th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Deployment names don’t have to be unique per OS –** It is now possible to create a deployment with the same name as an existing deployment, provided the operating system being deployed to is different.
* **New “Product Docs” and “Release Notes” options added to the support menu –** Now when you click the Support Menu (**?**) you’ll see links to both the PMPC Cloud **Product Docs** and **Release Notes** to help you find the information you need to work with and keep up-to-date on what we’re doing with PMPC Cloud.
* **Changing certain settings on a deployment now warns you we are resetting other values –** Now if you change settings such as the installer type, architecture or installation context, you’ll be warned that doing so will reset all configurations from the other tabs because some settings are only available for specific options.

</details>

<details>

<summary>Fixes</summary>

#### Custom Apps

* Resolved an issue with browser hangs or crashes when uploading a large number of extra files.
* Resolved an issue with a **Reload site** prompt being displayed in error when saving a Custom App.

</details>

### Week of March 5th, 2025

No release.

### Week of February 26th, 2025

<details>

<summary>New Features</summary>

#### Intune Apps

* **LOB support added for macOS –** We now support deploying macOS Line-of-Business (LOB) apps.

</details>

<details>

<summary>Fixes</summary>

#### Custom Apps

* Resolved an issue with being unable to upload files of 0 bytes using the **Extra Files** feature.

#### Intune Apps

* Resolved an issue when uploading Extra Files using the **Add Folder** option, where if multiple files exist in any subfolder and they have the same hash, you see **Error File with the same hash already exists**.&#x20;

</details>

### Week of February 19th, 2025

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with a Webhook notification showing as "Failed" for an Update Ring that was created successfully.

</details>

### Week of February 12th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Improvements to ESP Profiles workflow**
  * You can no longer add an ESP Profile containing 100 or more apps to a deployment.
  * If you and a single **Update Only** assignment to a deployment configured to use ESP Profiles, the **Configurations** tab is marked with a red “**X**” to indicate there is an issue.
* **Improved retry mechanism for deployments**

</details>

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with the Terms and conditions not being displayed when entering an MSP Plus license key.
* Resolved an issue with a user assigned the **Custom App Admin** role receiving a **Validation Error** when logging into an MSP Customer.

</details>

### Week of February 5th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Uninstall assignment type unsupported on macOS for PKG files –** Now when you deploy a .PKG file to macOS, we do not allow you to use the **Uninstall** assignment type.

#### Custom Apps

* Prevent an app deployment from being deleted from a parent MSP company if it is deployed at any child companies.

</details>

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with multiple copies of the daily deployment notification emails being sent with different content. We now check for the status of the deployment before sending the email and don’t include any deployments with a status of “Unknown.”

#### Custom Apps

* Resolved an issue with Custom Apps being unavailable in the App Catalog with users assigned the **Custom Apps Admin** role.

</details>

### Week of January 29th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Custom Pre and Post Scripts naming –** Now, if you upload a custom pre or post script to use in a deployment, we maintain the custom name rather than renaming it to a standard name.
* **Context Sensitive Searching is now supported in Scope Tags –** You can now type in the **Profile Name** field and we’ll automatically return a list of matching Scope Tags.

</details>

<details>

<summary>Fixes</summary>

#### Portal

* You can no longer disconnect a child company from an MSP Parent if there is not at least one user granted the **Full Admin with Access Management** role in the child company.
* Resolved an issue with Events not being written when pausing a deployment.

</details>

### Week of January 22nd, 2025

<details>

<summary>Fixes</summary>

#### Custom Apps

* Resolved an issue when changing the name of a vendor with mixed case, the name wasn’t saved to the Application Catalog. If the app is subsequently edited, the old, incorrect name is shown.

</details>

### Week of January 15th, 2025

<details>

<summary>New Features</summary>

#### Custom Apps

* Ability to upload additional files and folders when creating/editing a Custom App.

</details>

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with the **Update Only** App assignment type not being present for Custom Apps.&#x20;
* Resolved an issue where if the **EnforcedUninstallArgument** was saved in the App Catalog, it was not used when creating an uninstall in a deployment

#### Intune Apps

* Resolved an issue with not being able to upload extra files with no name and just an extension.

</details>

### Week of January 8th, 2025

<details>

<summary>New Features</summary>

#### Portal

* **Extra Files –** We now support uploading files with the same name, provided they are in different folders. We also support uploading folders with the same name, provided the selected paths are unique.

</details>

### Week of January 2nd, 2025

<details>

<summary>Fixes</summary>

#### Intune Apps

* Resolved an issue with Update Rings where rings with retried deployments were duplicated in the daily notification email.

</details>

### 18th December 2024

#### New Features

#### Portal

* **Entra ID Security Groups -** The ability to use [Entra ID Security Groups](cloud-administration/manage-cloud-users/using-entra-id-security-groups-in-cloud/) feature is now generally available (GA).
* **App Dependencies -** The [Dependencies ](cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/dependencies-deployments.md)feature is now avialble in Public Preview.

#### Fixes

#### Binary Free Apps

* Resolved an issue with the validation for the **Additional Argument** field of a deployment not working correctly.

### 11th December 2024

#### Fixes

#### Portal

* Resolved an issue where an error was displayed when a user with the Read-only Admin role enables Pause Updates.

### 4th December 2024

#### New Features

#### Portal

* **Create a Deployment with No Assignments -** [This feature](cloud-deployments/create-a-cloud-deployment-without-assignments.md) has now been released.
* **Entra ID Security Groups -** The ability to use [Entra ID Security Groups](cloud-administration/manage-cloud-users/using-entra-id-security-groups-in-cloud/) feature is now in Public Preview.
* **Extra Files -** The [Extra Files](cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/extra-files-deployments.md) feature (also known as _Deployment configuration files_) is now in Public Preview.

#### Fixes

#### Portal

* Resolved an issue with the portal not auto-refreshing the **Status** when creating a new deployment.

### 27th November 2024

#### New Features

#### Portal

* **New Visual Indicator for Public Preview Features –** If you have [enabled Preview Features](cloud-administration/manage-your-cloud-company/enable-cloud-preview-features.md) in your PMPC Cloud company, we now show you how many and which Public Preview features you have enabled.

### 20th November 2024

#### New Features

#### Intune Apps

* **Support for Role Scope Tags -** We now support [Intune Role Scope Tags.](cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/role-scope-tags-optional.md)
* **Ability to enable auto-updates for an app –** If an app supports auto-updates, you can now choose whether to enable this behavior.
* **Script name auto-populated –** Now when you now import a script to a deployment, the **Script Name** field is auto-populated with the script’s name.

#### Fixes

#### Custom Apps

* Resolved an issue where Webhook notifications were not sent for some Update Rings.

### 13th November 2024

#### New Features

#### Portal

* **Restriction on M365x Tenants Starting a Trial -** We no longer allow customers whose Entra ID domain starts with **m365x** to start a Patch My PC (PMPC) Cloud trial. Such customers will not see the option to start a PMPC Cloud Trial and will either need to enter a PMPC Cloud license key or activate their license using their on-premises Publisher license ke&#x79;_._

#### Fixes

#### Custom Apps

* Resolved an issue with Custom Apps becoming “stuck” or taking a long time to be created.

#### Intune Apps

* Resolved an issue with old versions of apps not being deleted from Update Rings.
* Resolved an issue with being unable to connect to Intune after deleting the connection for a linked MSP company.

### 6th November 2024

#### New Features

#### Portal

* **New service unavailable notification –** If one of our regional services is unavailable, you will now see a banner notification informing you of this.

#### Fixes

#### Portal

* Resolved an issue where enabling email notifications resulted in the first email showing all historical information, not just the relevant notifications.
* Resolved an issue with webhook notifications not being received if the payload exceeds 28kb.

### 30th October 2024

#### New Features

#### Intune Apps

* Various improvements to the daily update report email.

#### Fixes

#### Portal

* Resolved an issue with the **Install and Update App** no assignment type being available incorrectly when deploying a .MSP file.
* Resolved an issue with icons not appearing in AppCat after adding an app.

#### Intune Apps

* Resolved an issue where the **Add Assignment** button is unavailable if the Entra group for an existing assignment has been deleted from Entra. We now display an error and force you to remove the assignment in this scenario.

### 23rd October 2024

#### New Features

#### Intune Apps

* Maximum delay for an Update Ring has been increased to 180 days.
* Improved overall [language support](https://docs.patchmypc.com/installation-guides/patch-my-pc-cloud/deployments/deployment-wizard-reference#language)

#### Fixes

#### Intune Apps

* Resolved an issue where the email and webhook notifications were not received after creating a deployment with no assignments.

### 16th October 2024

#### New Features

#### Portal

* **New .MSP Installer Type added to AppCat –** We now support the .msp installer type in AppCat.
* **New “Read-Only Admin” user role –** This new role can view all pages in the portal but cannot make any changes. This role is intended for audit purposes.
* **New “Tenant Recovery” option –** If enabled, prevents a PMPC Company from being recovered using the [Recover Your Company](cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) process.\
  &#xNAN;_\[**NOTE:** You will need to contact support to get this feature enabled due to the potential consequences of enabling it.]_
* **Deployment method icon shown in Discovery –** When you view the **Managed** tab of Discovery, we show the method used to deploy the app i.e. PMPC Cloud, on-premises Publisher, or both.
* **Cooldown Timer for Company Recovery –** Recovering a company is now limited to three attempts every 12 hours.

#### Intune Apps

* **Warning when changing from Daily Sync Schedule –** We now have a new warning when changing your Sync Schedule from **Daily** as this can affect how Update Rings work.
* **Update Rings Deployment Summary warns if you are not using a Daily Sync Schedule –** When creating or editing a deployment that uses Update Rings, the **Deployment Summary** popup includes a warning against using anything but a **Daily** Sync Schedule with Update Rings.
* **Update Rings now detects the Sync Schedule –** If the Sync Schedule is configured to run on anything but a **Daily** schedule, Update Rings now forces the delay between Update Rings to align with the Sync Schedule.

#### Fixes

#### Portal

* Resolved an issue with the user’s first name and last name fields not being automatically populated on sign-up.

#### Custom Apps

* Resolved the **Unable to deploy. Product data was not found** error.

### 9th October 2024

#### New Features

#### Intune Apps

* **Deployments without assignments –** You can now create a deployment without assignments\
  \[_**Note:** You need to be using the Update Rings Feature currently in Public Preview to be able to use this functionality_].
* **Update Rings can now be updated at the Ring level –** You can now update a ring to any available version that is higher than the current version.

### 2nd October 2024

#### New Features

#### Portal

* **Discovery now shows the icon for an app –** [Discovery](discovery-in-cloud/) now shows the relevant icon for each app that’s managed/unmanaged.
* **Daily Updates Email Report includes newly created Deployments –** The daily Updates Report now includes the details of any new deployments created in the previous 24 hours \[_**Note:** You need to be using the Update Rings Feature currently in Public Preview to receive the report with these improvements_].

### 25th September 2024

#### New Features

#### Portal

* **Discovery now shows Publisher apps –** The **Managed** tab of [Discovery](discovery-in-cloud/) now includes apps deployed by our on-premises Publisher.
* **Recommended default name for the Branding App –** We now provide a recommended default name for the branding app, which you can override.

#### Intune Apps

* **Update Rings \[PUBLIC PREVIEW] -** The [Update Rings](cloud-deployments/cloud-update-rings/) feature of Patch My PC (PMPC) Cloud allows you to deploy apps and updates in a phased manner across your Intune estate.
* **Increased number of characters for Additional Arguments -**  The maximum number of characters you enter in this field has been increased to 500.

#### Fixes

#### Portal

* **Resolved truncating issue with App Cat app names –** When opened, apps with long names are no longer truncated but are displayed in full on the app’s properties page.

#### Binary Free Apps

* **Resolved “No Files Added” bug –** After uploading a new version of the app.

### 17th September 2024

#### New Features

#### Portal

* **Discovery –** The [Discovery ](discovery-in-cloud/)feature is now available in Public Preview. This feature lets you see which apps in our App Catalog are installed in your environment, including any Binary Free Apps or Custom Apps you may have added.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>As this is a preview feature, you must [Enable Preview Features](cloud-administration/manage-your-cloud-company/enable-cloud-preview-features.md) for the **Discovery** node to appear in your portal.</p>
</blockquote>

* **Folder installation log now shown –** We now show the path to the installation log in the new **Installation Logging** section of the **Summary** tab. We currently do not support changing this.

#### Fixes

#### Portal

* **Sync Schedule –** GMT is no longer shown in the UI of the [Sync Schedule](cloud-administration/manage-the-sync-schedule-in-cloud.md) to avoid confusion.

### 11th September 2024

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>No public facing changes were made on the 4th September.</p>
</blockquote>

#### New Features

#### Portal

* **Company ID shown during recovery –** When you [recover a company](cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md), we now include the company ID as well as the name of any companies you can recover in the **Company to Claim** dropdown.

#### Fixes

#### Intune Apps

* **Vendor Verbose Logging enabled –** Resolved an issue with vendor verbose logging not being enabled by default for IntuneSync.
* **On Restart Notifications incorrectly configured –** Resolved an issue where if the notifications for a deployment are configured for **On Restart**, the **Show All** option is actually selected on the dropdown, and not **On Restart**.

### 28th August 2024

#### New Features

#### Portal

* **Recover Your Company –** We now provide a facility for you to regain access to your company by using the new [Recover Your Company](cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) process.

### 21st August 2024

#### New Features

#### Portal

* **Latest Version added to app properties –** Now when you open an app’s properties, we show the latest version number.

#### Binary Free Apps

* **Link to vendor download –** When you upload the installer, we now provide a link to the official vendor’s website to ensure you download the most recent and official version.

### 14th August 2024

#### Fixes

#### Portal

* **Notifications –** Resolved an issue with emails not being sent for some apps after the daily sync job ran.
* **Users –** Resolved an issue where changing a user’s role resulted in several notification emails being sent instead of one.

#### Intune Apps

* **Naming Conventions –** Resolved an issue where any tag added after a string was not recognized.

### 7th August 2024

#### New Features

#### Portal

* Link to product documentation added to the support menu.
* **Users –** The portal now displays a confirmation if you try deleting yourself.

#### Custom Apps

* **Improved App Icon UI –** We now show the supported file types in the UI for the **App Icon**.

#### Intune Apps

* **Improved language support -** English variants are now exposed. Previously, we only exposed **English** as a language for apps. We now expose all available variants such as **English - Canada**, **English - United Kingdom**, **English - United States**, etc.

### 31st July 2024

#### New Features

#### Intune Apps

* **Update-only assignments for user-based apps –** You can now create update-only assignments/packages with Intune Apps in the same way as you can with our OnPrem Publisher.

#### Fixes

#### Custom Apps

* Resolved an issue with **Silent Install Parameters** not being copied over when adding a new version of an app.

### 24th July 2024

#### New Features

#### Portal

* **Sync Schedule changed to UTC –** To help avoid confusion, the **Sync Schedule** time is now based on [Coordinated Universal Time (UTC)](https://simple.wikipedia.org/wiki/Coordinated_Universal_Time).

#### Fixes

#### Portal

* **Customer Support –** Resolved an issue with being unable to edit a timer with less than 4 hours remaining.

#### Custom Apps

* **Deployments –** Resolved an issue with some Custom Apps being stuck with the status of **Retrying**.

### 17th July 2024

#### New Features

#### Portal

* **Ability to opt-in to Preview Features –** You can now opt-in to automatically gain access to pre-release features we mark as Public Preview.
* **Customer Support feature re-designed –** You can now set a timer to limit the amount of time Patch My Support has access to your environment and the level of access.
* **Test buttons for Notifications –** New buttons to allow you to send test notifications/emails when setting up Notifications to check they are configured correctly.

#### Intune Apps

* **Allow Available Uninstall –** You can now configure a deployment to allow an app installed by the Company Portal to be uninstalled by Intune Apps.
* **Increased upload limits for pre/post scripts –** Previously, the total size of all pre/post scripts for a deployment was limited to 1 MB. This has now been increased to 1 MB per script, with a total size limit of 4 MB.

#### Fixes

#### Portal

* **Deployments –** Resolved an issue with the Edit button not being displayed if an app has already been successfully deployed.

#### Custom Apps

* Resolved an issue with the MSI Product Code being displayed for a Custom App created with an EXE as the primary installer file.

### 10th July 2024

#### New Features

#### **Portal**

* **Improved sorting by column –** Columns can be sorted by more headings in various nodes when working in the portal.
* **Improved user access requests —** Users can now enter a message giving more information about why they are requesting access to a company.
* **Improved access denied flow  –** Admins can now provide a reason for declining a user's access request.
* **Revoking Access Management rights warning –** Now if you try to revoke Access Management rights for your account, provided at least one other account has this right, you will still be prompted if you are sure you wish to proceed.
* **Search –** General improvements to search.
* **Sync Schedule –** The new [Sync Schedule](https://docs.patchmypc.com/patch-my-pc-cloud/administration/managing-the-sync-schedule) feature allows you to set a different time and frequency for the sync job to run.

#### Fixes

* **Branding –** Resolved an issue where uploading a new logo with the same name as the existing one shows the old logo.
* **Notifications –** Resolved an issue with Teams and Slack notifications cutting off CVE data and not containing release notes.
* **Update reports –** Resolved an issue with the formatting of file sizes on the deployment email report.

### 3rd July 2024

#### New Features

#### Portal

* **Users –** Now you cannot remove the **Access Management** right for the last admin user in your company. This prevents you from locking yourself out of the portal. If you are the last user and there is at least one other account with this right, if you try revoking it from your account, you are prompted to confirm because of the consequences.
* **Users –** The **Application Deployment Admin** user role has been renamed **Intune App Admin**.

#### Intune Apps

* **Naming Conventions -** You can now use the new [Naming Conventions](cloud-administration/manage-cloud-naming-conventions/) feature to configure custom naming conventions for all deployments created in Intune Apps for Cloud. This allows you to standardize the naming convention across all your Intune deployments.

#### Fixes

#### Portal

* **Deployments –** Resolved an issue with two Update-only apps being created in Intune if the first one fails. Now, if an app fails to be created in Intune, we delete it.
* **Onboarding –** Resolved a sign-in issue when a user accepts an invitation.

#### Custom Apps

* Resolved an issue with the **Naming** page not being accessible.

### 26th June 2024

#### New Features

#### Portal

* New [Intune App Admin ](https://docs.patchmypc.com/patch-my-pc-cloud/reference/user-roles)user role added.
* **General –** Clicking our logo in the top left-hand corner of the portal returns you to the App Catalog and forces a refresh.

#### Fixes

#### Portal

* **App Catalog –** If the name of an app is truncated, hovering over it now shows the full name as a tooltip.
* **Contact Form –** Resolved a memory exception error when sending attachments to us through the Contact Form in the portal. You can now send up to 25 MB of attachments when using this form.
* **Deployments –** Resolved issues :
  * with **Pause Updates** being disabled when editing an existing deployment where **Pause Updates** has been enabled.
  * when editing a deployment, any required assignments with an availability date set to **ASAP** are not modified until the next day at 12 AM.
* **Deployment Filters –** When adding a deployment filter to an app deployment, we now only show filters for the **Windows 10 and later** platform, instead of all filters.
* Various improvements to notification messages and tooltips to improve readability.

#### Custom Apps

* Resolved an issue with the user being able to add the same conflicting process multiple times when creating a Custom App. We now do validation to prevent this.

### 19th June 2024

#### New Features

#### Portal

* **Contacting Support –** You can now modify the **From** email address when using the [Contact Support](https://docs.patchmypc.com/patch-my-pc-cloud/contacting-support) form.
* **Environments node –** New [Reconnect ](https://docs.patchmypc.com/patch-my-pc-cloud/administration/managing-your-environments/managing-intune-tenants#reconnecting-an-intune-tenant)button added under the **Intune** connection.
* **Licensing –** If you already have an active license with us and click **Start Trial**, we detect this and use your existing license to activate your portal.
* **Notifications node –** New tooltips have been added so you know when you will receive notifications.
* Primary buttons in the UI re-designed based on user feedback.

#### Fixes

* Various improvements to notification messages and tooltips to improve readability.

### 5th June 2024

#### Fixes

* The “**Prevent from opening an application while the application is updating**” checkbox is no longer checked by default on the **Conflicting Processes** settings pop-up.
* Resolved an issue with the configuration of Conflicting Processes not being honored.
* Various other bugs.