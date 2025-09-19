---
description: Test Cloud Release Notes here
---

# Cloud Release Notes

_Applies to: Patch My PC Cloud_

Details the production release history for Patch My PC (PMPC) Cloud, the most recent release being shown first.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>We aim to release new features, updates, and fixes at 12:00 CEST every Wednesday.</p>
<p>_Production Release_ means we have released that item to our Production environment i.e. customers can access it, although a specific feature maybe in one of the following three production states:\</p>
<p>* Private Preview, which is invitation only.</p>
<p>* Public Preview for which you will need to have [Preview Features enabled](cloud-administration/manage-your-cloud-company/enable-cloud-preview-features.md) in your company to access it.</p>
<p>* General Availability which is available to everyone.&#x20;</p>
<p>Please see the relevant docs for a feature for more information which will indicate the state of the feature.</p>
<p>You can also access this page from within the Cloud Portal by clicking the support button (!["support" button](/_images/image-(587).png>)) in the header area and selecting <strong>Release Notes</strong>.</p>
</blockquote>

### Week of August 6<sup>th</sup>, 2025

#### New Features

<strong>Portal</strong>

* <strong>Customer Feedback –</strong> Now, when you complete certain workflows for the first time, we give you the option of providing feedback on your experience.

<strong>Managed Service Provider</strong>

* <strong>MSP Invites –</strong> Managed Service Providers (MSPs) can now send invitation links to customers, allowing them to self-register and create their own companies within the system to be managed by the MSP

#### Fixes

<strong>Portal</strong>

* Resolved an issue where the ConfigMgr version of an app migrated to PMPC Cloud was deployed instead of the newer version in our App Catalog.

<strong>Binary Free Apps</strong>

* Resolved an issue where if a customer uploaded a newer version of an app, an older version was deployed.

### Week of July 30th,  2025

<details>

<summary>New Features</summary>

<strong>Custom Apps</strong>

* <strong>Uninstall Arguments –</strong> We’ve now added the ability for you to specify uninstall parameters for a Custom App.

<strong>Intune Apps</strong>

* <strong>PMPC Scripts –</strong> You can now see and disable any scripts we recommend for an app when you create a deployment.

<strong>Managed Service Provider</strong>

* <strong>App Set Details –</strong> You can now expand an App Set to see a list of the apps it contains and summary information for each app within the App Set.

</details>

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue with Microsoft SQL Server Management Studio 21, where assignments could only be created to either install or update this app. Now we support both.

<strong>Custom Apps</strong>

* Resolved an issue when creating a Custom App containing files with duplicate names but different extensions (e.g. <strong>setup.exe</strong> and <strong>setup.zip</strong>), generating a duplicate filename error.

<strong>Intune Apps</strong>

* Resolved an issue where attempting to add an assignment to an existing deployment failed with a <strong>400 Bad Request</strong> error.

<strong>Managed Service Provider</strong>

* Resolved an issue where adding a Child MSP company to an App Set containing a Custom App resulted in the app being stuck with a status of <strong>In Progress</strong> on the Child Company.
* Resolved an issue where adding a Child MSP company generated a <strong>Bad request</strong> error.

</details>

### Week of July 23rd,  2025

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue with some users receiving an “<strong>An error occurred while processing your request</strong>” when working with Branding.
* Resolved an issue with a <strong>Limit</strong> showing as red when it reached 99%, not 100%.
* Resolved an issue with a Discovery data failing to load, sometimes with a <strong>TypeError: Failed to fetch</strong> error.

<strong>Custom Apps</strong>

* Resolved an issue with Custom Apps getting stuck at stage of 3/3 after editing.

<strong>Managed Service Provider</strong>

* Resolved an issue with assignments not being shown correctly for MSP App Sets.

</details>

### Week of July 16th,  2025

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue where if the macOS trial banner was closed for one PMPC Cloud Company, if you logged into another company, the banner was also disabled.
* Resolved an issue with overlapping elements in the portal if a resolution lower than 1324 x 724px was used.
* Resolved an issue where if you had the <strong>Remember my Selection</strong> checkbox checked on the sign in page, then signed out, and selected a different company to sign into, you were signed into the company that was remembered, not the new one you selected to sign into.

<strong>Custom Apps</strong>

* Resolved an issue with an app’s icon not being displayed in a webhook when the deployment of a Custom App is updated via the Sync Schedule.

<strong>Intune Apps</strong>

* Resolved an issue when running Discovery for a new PMPC Cloud Company generating an error, which was resolved by clicking <strong>Refresh</strong>.
* Resolved an issue with the sorting of apps in Discovery not working correctly.
* Resolved an issue with excluding an Entra ID group from Branding now working.

<strong>Managed Service Provider</strong>

* Resolved an issue with adding a scripts and arguments to an MSP App Sets not being saved, as when you edited the App Set, the script and it’s arguments were missing.

</details>

### Week of July 9th,  2025

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue with <strong>Company Recovery</strong> being referred to as <strong>Tenant Recovery</strong> in the <strong>Events</strong> section.

</details>

### Week of July 2<sup>nd</sup>, 2025

<details>

<summary>New Features</summary>

<strong>Portal</strong>

* <strong>New “Items per page” options –</strong> We’ve added new values to the <strong>Items per page</strong> dropdown in the portal to allow you to choose to display more items per page in the portal.
* <strong>Increased character limits –</strong> We now support 2,048 characters in the following fields:
  * Install Parameters Additional Argument
  * Silent Install Parameters
  * Additional Silent Uninstall Parameters

<strong>Custom Apps</strong>

* <strong>Version number replaced with “%” –</strong> Now, when you add a Primary Install File that is an MSI, when populating the various properties, if we detect a version number in the <strong>Apps & Features Name</strong> field, we replace it with a "<strong>%</strong>".

</details>

<details>

<summary>Fixes</summary>

<strong>Discovery</strong>

* Resolved an issue where if a single Intune discovered app was mapped to two different products from our App Catalog, and one of them was managed and the other was unmanaged, one of them would appear under the <strong>Managed</strong> tab and the other would appear in the <strong>Unmanaged</strong> tab.\
  \
  Now, if one of them is managed and the other is unmanaged, the managed app is displayed in the <strong>Managed</strong> tab and the unmanaged app is hidden in the <strong>Unmanaged</strong> tab.\


<strong>Custom Apps</strong>

* Resolved an issue with a Custom Apps icon not being shown in a webhook when its deployment is updated via Sync Schedule.

<strong>Managed Service Provider</strong>

* Resolved an issue with an MSP not being able to unlink a child customer if their license had expired.

</details>

### Week of June 25<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

<strong>Portal</strong>

* <strong>New "Usage" page –</strong> We now show the usage limits for your PMPC Cloud company and your current usage to allow you to see when what you are using and when you are approaching a limit.
* <strong>New tooltip for MSP deployments –</strong> Now if you select the <strong>.msp</strong> installer when creating a deployment, we pop-up a warning that you will only be able add an Update Only assignment to this deployment and you should select the <strong>.exe</strong> installer if you want to use the other assignment types.
* <strong>New default variant logic –</strong> We’ve now replaced our existing language-only priority when creating a deployment with logic based on language, installation context, architecture, and installer type.

</details>

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue with Entra ID Groups not being sorted alphabetically in the portal when searching to add them to an assignment.

</details>

### Week of June 18<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

<strong>Portal</strong>

* <strong>Granting PMPC Support Access –</strong> We now provide a dropdown to allow you to choose the number of hours you want to grant our Support Team access to your PMPC Cloud company.

</details>

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue when sorting by operating system within Discovery not sorting correctly.

</details>

### Week of June 11<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

<strong>Portal</strong>

* <strong>Improved UI for multi-versions –</strong>&#x4E;ow if an app has multiple versions in the App Catalog that can be deployed, we indicate the number of versions available and allow you to select the relevant version you want to deploy from a dropdown on the app’s tile in the App Catalog.

<strong>Intune Apps</strong>

* <strong>Ability to create an "Uninstall Branding" app –</strong> You can now create this app which will create an Intune Win32 app, assigned as required with an uninstall intent, to remove any custom branding files from devices.

</details>

<details>

<summary>Fixes</summary>

<strong>Intune Apps</strong>

* Resolved an issue where a user could create a Windows Deployment Template with an ESP Profile and an Update Only Assignment. It should not be able to create such a combination.

</details>

### Week of June 4<sup>th</sup>, 2025

<details>

<summary>New Features</summary>

<strong>Binary Free Apps</strong>

* <strong>Improved validation –</strong> Previously, you could upload one bitness of an app, but attempt to deploy a different bitness. It was only when you got to the end of the Deployment Wizard that we informed you of this mismatch.

</details>

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue with the text entered in the <strong>Reason for Request</strong> field when requesting access to a PMP Cloud Company not being populated in the portal.

</details>

### Week of May 28th, 2025

<details>

<summary>New Features</summary>

<strong>Intune Apps</strong>

* <strong>Improved error handling for deployments when permissions are removed –</strong> We have improved error handling for various deployment-related scenarios when permissions are either removed or amended when managing deployments.

</details>

<details>

<summary>Fixes</summary>

<strong>Intune Apps</strong>

* Resolved an issue with the incorrect error message being displayed when Company limits have been reached. We now show the correct error for the relevant cause.

</details>

### Week of May 21st, 2025

<details>

<summary>New Features</summary>

<strong>Portal</strong>

* <strong>Templates –</strong> You can now set the default type of Update Rings from within a Template.
* <strong>Templates –</strong> The <strong>Tools</strong> menu has been added to the <strong>Configurations</strong> page of templates to make it easier for you to navigate the various available sections.

</details>

<details>

<summary>Fixes</summary>

<strong>Portal</strong>

* Resolved an issue with the list of languages on the <strong>Branding List</strong> page showing the language that was configured first when it should be the default language.
* Resolved an issue where inserting a variable in the middle of text when defining naming standards actually inserted the variable at the end of the field and not at the chosen point in the text.
* Resolved an issue with <strong>Exclude</strong> filters configured on a deployment actually being applied as an <strong>Include</strong> filter.

<strong>Intune Apps</strong>

* Resolved an issue with Scope Tags manually added in Intune not being copied forward.

</details>

### Week of May 14th, 2025

<details>

<summary>New Features</summary>

Portal

* <strong>Change to Self-Update template behavior –</strong> Now when you create a Template, we check the <strong>Disable Self-Update</strong> option under the <strong>Built-in Auto Updates</strong> section by default (previously this was unchecked).
* <strong>Change to Company Recovery option –</strong> We’ve changed the language used for the <strong>Company Recovery</strong> section on the <strong>Company</strong> page to make it clearer.
* <strong>New Update rings start time dropdown –</strong> Previously, when creating a deployment, on the <strong>Assignments</strong> page, after clicking <strong>Enable Update Rings</strong> you had the choice of choosing to create either <strong>Delayed</strong> or <strong>Immediate</strong> rings. We’ve now moved the choices under a new <strong>Update rings start time</strong> dropdown, recommending <strong>Delayed</strong> and including tooltips to help guide you.

</details>

<details>

<summary>Fixes</summary>

<strong>Custom Apps</strong>

* Various bugs squashed to resolve issues with deployments getting stuck.
* Resolved an issue with the <strong>Custom App Admin</strong> not having access to the <strong>App Catalog</strong> page.

<strong>Intune Apps</strong>

* Resolved an issue with two deployments being created in Intune after a deployment with No Assignments is recreated.
* Various bugs squashed to resolve issues with deployments getting stuck.

</details>

### Week of May 7th, 2025

<details>

<summary>Fixes</summary>

<strong>Intune Apps</strong>

* Resolved an issue when adding extra files to an existing deployment (either through editing it or adding a new version) of those files missing from the deployment.
* Resolved an issue with config files larger than 28.6 MB failing to upload.

</details>

### Week of April 30th, 2025

<details>

<summary>New Features</summary>

#### Custom Apps

* <strong>Improved error handling for macOS Custom Apps –</strong> Previously, if you uploaded a <strong>.pkg</strong> or <strong>.dmg</strong> file as the primary installer file, we just showed an "<strong>unsupported file</strong>" notification. We now show the following notification:\
  "Custom Apps for macOS are not supported at this time. Vote and subscribe to [PMPC Cloud Portal - macOS Custom Apps](https://ideas.patchmypc.com/ideas/PATCHMYPC-I-6056) to receive updates on future development."

</details>

<details>

<summary>Fixes</summary>

#### Intune Apps

* Resolved an issue with Detection Rules when configuring the time for a <strong>Date Modified</strong> rule, where if a PM time was selected, it was actually saved as the corresponding AM time.

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

* <strong>Recommend App Dependencies now shown –</strong> When you now create an App Dependency, we automatically show a list of recommended apps (if relevant) that you should consider configuring as dependencies for the app being deployed.

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

* <strong>Additional filters added to help when working with Deployments –</strong> The filter list in the portal now includes new filters to only show which deployments are using Update Rings (enabled or disabled) as well as which deployments have updates paused or not.

</details>

### Week of April 2nd, 2025

<details>

<summary>New Features</summary>

#### Portal

* <strong>UI improvements for Deployment Properties –</strong> We’ve improved the UI when looking at the properties of a deployment so as not to truncate entries such as script names.

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

* Resolved an issue with users not being notified of a new version of an app being available if either the <strong>Notify All Users in Company</strong> or <strong>Notify Specific Users</strong> options are selected.

#### Custom Apps

* Resolved an issue when uploading extra files with the same name but in different folders, the UI didn’t process the folder structure and instead uploaded all of the files as independent files.

</details>

### Week of March 19th, 2025

<details>

<summary>New Features</summary>

#### Portal

* <strong>Number of available versions now shown for apps in the App Catalog –</strong> If multiple versions are available for different variants of the same app, App Cat will show the number of available versions. If you hover over the number, you can see the list of variants grouped accordingly. If only one version is available for all variants, only that version will be displayed.

#### Intune Apps

* <strong>Native Detection Rules –</strong> Patch My PC (PMPC) Cloud deployments now support Native Detection Rules.
* <strong>Pre/Post Scripts now support Arguments –</strong> Our Pre and Post Scripts now support additional arguments.

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

* <strong>Deployment names don’t have to be unique per OS –</strong> It is now possible to create a deployment with the same name as an existing deployment, provided the operating system being deployed to is different.
* <strong>New “Product Docs” and “Release Notes” options added to the support menu –</strong> Now when you click the Support Menu (<strong>?</strong>) you’ll see links to both the PMPC Cloud <strong>Product Docs</strong> and <strong>Release Notes</strong> to help you find the information you need to work with and keep up-to-date on what we’re doing with PMPC Cloud.
* <strong>Changing certain settings on a deployment now warns you we are resetting other values –</strong> Now if you change settings such as the installer type, architecture or installation context, you’ll be warned that doing so will reset all configurations from the other tabs because some settings are only available for specific options.

</details>

<details>

<summary>Fixes</summary>

#### Custom Apps

* Resolved an issue with browser hangs or crashes when uploading a large number of extra files.
* Resolved an issue with a <strong>Reload site</strong> prompt being displayed in error when saving a Custom App.

</details>

### Week of March 5th, 2025

No release.

### Week of February 26th, 2025

<details>

<summary>New Features</summary>

#### Intune Apps

* <strong>LOB support added for macOS –</strong> We now support deploying macOS Line-of-Business (LOB) apps.

</details>

<details>

<summary>Fixes</summary>

#### Custom Apps

* Resolved an issue with being unable to upload files of 0 bytes using the <strong>Extra Files</strong> feature.

#### Intune Apps

* Resolved an issue when uploading Extra Files using the <strong>Add Folder</strong> option, where if multiple files exist in any subfolder and they have the same hash, you see <strong>Error File with the same hash already exists</strong>.&#x20;

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

* <strong>Improvements to ESP Profiles workflow</strong>
  * You can no longer add an ESP Profile containing 100 or more apps to a deployment.
  * If you and a single <strong>Update Only</strong> assignment to a deployment configured to use ESP Profiles, the <strong>Configurations</strong> tab is marked with a red “<strong>X</strong>” to indicate there is an issue.
* <strong>Improved retry mechanism for deployments</strong>

</details>

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with the Terms and conditions not being displayed when entering an MSP Plus license key.
* Resolved an issue with a user assigned the <strong>Custom App Admin</strong> role receiving a <strong>Validation Error</strong> when logging into an MSP Customer.

</details>

### Week of February 5th, 2025

<details>

<summary>New Features</summary>

#### Portal

* <strong>Uninstall assignment type unsupported on macOS for PKG files –</strong> Now when you deploy a .PKG file to macOS, we do not allow you to use the <strong>Uninstall</strong> assignment type.

#### Custom Apps

* Prevent an app deployment from being deleted from a parent MSP company if it is deployed at any child companies.

</details>

<details>

<summary>Fixes</summary>

#### Portal

* Resolved an issue with multiple copies of the daily deployment notification emails being sent with different content. We now check for the status of the deployment before sending the email and don’t include any deployments with a status of “Unknown.”

#### Custom Apps

* Resolved an issue with Custom Apps being unavailable in the App Catalog with users assigned the <strong>Custom Apps Admin</strong> role.

</details>

### Week of January 29th, 2025

<details>

<summary>New Features</summary>

#### Portal

* <strong>Custom Pre and Post Scripts naming –</strong> Now, if you upload a custom pre or post script to use in a deployment, we maintain the custom name rather than renaming it to a standard name.
* <strong>Context Sensitive Searching is now supported in Scope Tags –</strong> You can now type in the <strong>Profile Name</strong> field and we’ll automatically return a list of matching Scope Tags.

</details>

<details>

<summary>Fixes</summary>

#### Portal

* You can no longer disconnect a child company from an MSP Parent if there is not at least one user granted the <strong>Full Admin with Access Management</strong> role in the child company.
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

* Resolved an issue with the <strong>Update Only</strong> App assignment type not being present for Custom Apps.&#x20;
* Resolved an issue where if the <strong>EnforcedUninstallArgument</strong> was saved in the App Catalog, it was not used when creating an uninstall in a deployment

#### Intune Apps

* Resolved an issue with not being able to upload extra files with no name and just an extension.

</details>

### Week of January 8th, 2025

<details>

<summary>New Features</summary>

#### Portal

* <strong>Extra Files –</strong> We now support uploading files with the same name, provided they are in different folders. We also support uploading folders with the same name, provided the selected paths are unique.

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

* <strong>Entra ID Security Groups -</strong> The ability to use [Entra ID Security Groups](cloud-administration/manage-cloud-users/using-entra-id-security-groups-in-cloud/) feature is now generally available (GA).
* <strong>App Dependencies -</strong> The [Dependencies ](cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/dependencies-deployments.md)feature is now avialble in Public Preview.

#### Fixes

#### Binary Free Apps

* Resolved an issue with the validation for the <strong>Additional Argument</strong> field of a deployment not working correctly.

### 11th December 2024

#### Fixes

#### Portal

* Resolved an issue where an error was displayed when a user with the Read-only Admin role enables Pause Updates.

### 4th December 2024

#### New Features

#### Portal

* <strong>Create a Deployment with No Assignments -</strong> [This feature](cloud-deployments/create-a-cloud-deployment-without-assignments.md) has now been released.
* <strong>Entra ID Security Groups -</strong> The ability to use [Entra ID Security Groups](cloud-administration/manage-cloud-users/using-entra-id-security-groups-in-cloud/) feature is now in Public Preview.
* <strong>Extra Files -</strong> The [Extra Files](cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/extra-files-deployments.md) feature (also known as _Deployment configuration files_) is now in Public Preview.

#### Fixes

#### Portal

* Resolved an issue with the portal not auto-refreshing the <strong>Status</strong> when creating a new deployment.

### 27th November 2024

#### New Features

#### Portal

* <strong>New Visual Indicator for Public Preview Features –</strong> If you have [enabled Preview Features](cloud-administration/manage-your-cloud-company/enable-cloud-preview-features.md) in your PMPC Cloud company, we now show you how many and which Public Preview features you have enabled.

### 20th November 2024

#### New Features

#### Intune Apps

* <strong>Support for Role Scope Tags -</strong> We now support [Intune Role Scope Tags.](cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/role-scope-tags-optional.md)
* <strong>Ability to enable auto-updates for an app –</strong> If an app supports auto-updates, you can now choose whether to enable this behavior.
* <strong>Script name auto-populated –</strong> Now when you now import a script to a deployment, the <strong>Script Name</strong> field is auto-populated with the script’s name.

#### Fixes

#### Custom Apps

* Resolved an issue where Webhook notifications were not sent for some Update Rings.

### 13th November 2024

#### New Features

#### Portal

* <strong>Restriction on M365x Tenants Starting a Trial -</strong> We no longer allow customers whose Entra ID domain starts with <strong>m365x</strong> to start a Patch My PC (PMPC) Cloud trial. Such customers will not see the option to start a PMPC Cloud Trial and will either need to enter a PMPC Cloud license key or activate their license using their on-premises Publisher license ke&#x79;_._

#### Fixes

#### Custom Apps

* Resolved an issue with Custom Apps becoming “stuck” or taking a long time to be created.

#### Intune Apps

* Resolved an issue with old versions of apps not being deleted from Update Rings.
* Resolved an issue with being unable to connect to Intune after deleting the connection for a linked MSP company.

### 6th November 2024

#### New Features

#### Portal

* <strong>New service unavailable notification –</strong> If one of our regional services is unavailable, you will now see a banner notification informing you of this.

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

* Resolved an issue with the <strong>Install and Update App</strong> no assignment type being available incorrectly when deploying a .MSP file.
* Resolved an issue with icons not appearing in AppCat after adding an app.

#### Intune Apps

* Resolved an issue where the <strong>Add Assignment</strong> button is unavailable if the Entra group for an existing assignment has been deleted from Entra. We now display an error and force you to remove the assignment in this scenario.

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

* <strong>New .MSP Installer Type added to AppCat –</strong> We now support the .msp installer type in AppCat.
* <strong>New “Read-Only Admin” user role –</strong> This new role can view all pages in the portal but cannot make any changes. This role is intended for audit purposes.
* <strong>New “Tenant Recovery” option –</strong> If enabled, prevents a PMPC Company from being recovered using the [Recover Your Company](cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) process.\
  &#xNAN;_\[<strong>NOTE:</strong> You will need to contact support to get this feature enabled due to the potential consequences of enabling it.]_
* <strong>Deployment method icon shown in Discovery –</strong> When you view the <strong>Managed</strong> tab of Discovery, we show the method used to deploy the app i.e. PMPC Cloud, on-premises Publisher, or both.
* <strong>Cooldown Timer for Company Recovery –</strong> Recovering a company is now limited to three attempts every 12 hours.

#### Intune Apps

* <strong>Warning when changing from Daily Sync Schedule –</strong> We now have a new warning when changing your Sync Schedule from <strong>Daily</strong> as this can affect how Update Rings work.
* <strong>Update Rings Deployment Summary warns if you are not using a Daily Sync Schedule –</strong> When creating or editing a deployment that uses Update Rings, the <strong>Deployment Summary</strong> popup includes a warning against using anything but a <strong>Daily</strong> Sync Schedule with Update Rings.
* <strong>Update Rings now detects the Sync Schedule –</strong> If the Sync Schedule is configured to run on anything but a <strong>Daily</strong> schedule, Update Rings now forces the delay between Update Rings to align with the Sync Schedule.

#### Fixes

#### Portal

* Resolved an issue with the user’s first name and last name fields not being automatically populated on sign-up.

#### Custom Apps

* Resolved the <strong>Unable to deploy. Product data was not found</strong> error.

### 9th October 2024

#### New Features

#### Intune Apps

* <strong>Deployments without assignments –</strong> You can now create a deployment without assignments\
  \[_<strong>Note:</strong> You need to be using the Update Rings Feature currently in Public Preview to be able to use this functionality_].
* <strong>Update Rings can now be updated at the Ring level –</strong> You can now update a ring to any available version that is higher than the current version.

### 2nd October 2024

#### New Features

#### Portal

* <strong>Discovery now shows the icon for an app –</strong> [Discovery](discovery-in-cloud/) now shows the relevant icon for each app that’s managed/unmanaged.
* <strong>Daily Updates Email Report includes newly created Deployments –</strong> The daily Updates Report now includes the details of any new deployments created in the previous 24 hours \[_<strong>Note:</strong> You need to be using the Update Rings Feature currently in Public Preview to receive the report with these improvements_].

### 25th September 2024

#### New Features

#### Portal

* <strong>Discovery now shows Publisher apps –</strong> The <strong>Managed</strong> tab of [Discovery](discovery-in-cloud/) now includes apps deployed by our on-premises Publisher.
* <strong>Recommended default name for the Branding App –</strong> We now provide a recommended default name for the branding app, which you can override.

#### Intune Apps

* <strong>Update Rings \[PUBLIC PREVIEW] -</strong> The [Update Rings](cloud-deployments/cloud-update-rings/) feature of Patch My PC (PMPC) Cloud allows you to deploy apps and updates in a phased manner across your Intune estate.
* <strong>Increased number of characters for Additional Arguments -</strong>  The maximum number of characters you enter in this field has been increased to 500.

#### Fixes

#### Portal

* <strong>Resolved truncating issue with App Cat app names –</strong> When opened, apps with long names are no longer truncated but are displayed in full on the app’s properties page.

#### Binary Free Apps

* <strong>Resolved “No Files Added” bug –</strong> After uploading a new version of the app.

### 17th September 2024

#### New Features

#### Portal

* <strong>Discovery –</strong> The [Discovery ](discovery-in-cloud/)feature is now available in Public Preview. This feature lets you see which apps in our App Catalog are installed in your environment, including any Binary Free Apps or Custom Apps you may have added.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>As this is a preview feature, you must [Enable Preview Features](cloud-administration/manage-your-cloud-company/enable-cloud-preview-features.md) for the <strong>Discovery</strong> node to appear in your portal.</p>
</blockquote>

* <strong>Folder installation log now shown –</strong> We now show the path to the installation log in the new <strong>Installation Logging</strong> section of the <strong>Summary</strong> tab. We currently do not support changing this.

#### Fixes

#### Portal

* <strong>Sync Schedule –</strong> GMT is no longer shown in the UI of the [Sync Schedule](cloud-administration/manage-the-sync-schedule-in-cloud.md) to avoid confusion.

### 11th September 2024

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>No public facing changes were made on the 4th September.</p>
</blockquote>

#### New Features

#### Portal

* <strong>Company ID shown during recovery –</strong> When you [recover a company](cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md), we now include the company ID as well as the name of any companies you can recover in the <strong>Company to Claim</strong> dropdown.

#### Fixes

#### Intune Apps

* <strong>Vendor Verbose Logging enabled –</strong> Resolved an issue with vendor verbose logging not being enabled by default for IntuneSync.
* <strong>On Restart Notifications incorrectly configured –</strong> Resolved an issue where if the notifications for a deployment are configured for <strong>On Restart</strong>, the <strong>Show All</strong> option is actually selected on the dropdown, and not <strong>On Restart</strong>.

### 28th August 2024

#### New Features

#### Portal

* <strong>Recover Your Company –</strong> We now provide a facility for you to regain access to your company by using the new [Recover Your Company](cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) process.

### 21st August 2024

#### New Features

#### Portal

* <strong>Latest Version added to app properties –</strong> Now when you open an app’s properties, we show the latest version number.

#### Binary Free Apps

* <strong>Link to vendor download –</strong> When you upload the installer, we now provide a link to the official vendor’s website to ensure you download the most recent and official version.

### 14th August 2024

#### Fixes

#### Portal

* <strong>Notifications –</strong> Resolved an issue with emails not being sent for some apps after the daily sync job ran.
* <strong>Users –</strong> Resolved an issue where changing a user’s role resulted in several notification emails being sent instead of one.

#### Intune Apps

* <strong>Naming Conventions –</strong> Resolved an issue where any tag added after a string was not recognized.

### 7th August 2024

#### New Features

#### Portal

* Link to product documentation added to the support menu.
* <strong>Users –</strong> The portal now displays a confirmation if you try deleting yourself.

#### Custom Apps

* <strong>Improved App Icon UI –</strong> We now show the supported file types in the UI for the <strong>App Icon</strong>.

#### Intune Apps

* <strong>Improved language support -</strong> English variants are now exposed. Previously, we only exposed <strong>English</strong> as a language for apps. We now expose all available variants such as <strong>English - Canada</strong>, <strong>English - United Kingdom</strong>, <strong>English - United States</strong>, etc.

### 31st July 2024

#### New Features

#### Intune Apps

* <strong>Update-only assignments for user-based apps –</strong> You can now create update-only assignments/packages with Intune Apps in the same way as you can with our OnPrem Publisher.

#### Fixes

#### Custom Apps

* Resolved an issue with <strong>Silent Install Parameters</strong> not being copied over when adding a new version of an app.

### 24th July 2024

#### New Features

#### Portal

* <strong>Sync Schedule changed to UTC –</strong> To help avoid confusion, the <strong>Sync Schedule</strong> time is now based on [Coordinated Universal Time (UTC)](https://simple.wikipedia.org/wiki/Coordinated_Universal_Time).

#### Fixes

#### Portal

* <strong>Customer Support –</strong> Resolved an issue with being unable to edit a timer with less than 4 hours remaining.

#### Custom Apps

* <strong>Deployments –</strong> Resolved an issue with some Custom Apps being stuck with the status of <strong>Retrying</strong>.

### 17th July 2024

#### New Features

#### Portal

* <strong>Ability to opt-in to Preview Features –</strong> You can now opt-in to automatically gain access to pre-release features we mark as Public Preview.
* <strong>Customer Support feature re-designed –</strong> You can now set a timer to limit the amount of time Patch My Support has access to your environment and the level of access.
* <strong>Test buttons for Notifications –</strong> New buttons to allow you to send test notifications/emails when setting up Notifications to check they are configured correctly.

#### Intune Apps

* <strong>Allow Available Uninstall –</strong> You can now configure a deployment to allow an app installed by the Company Portal to be uninstalled by Intune Apps.
* <strong>Increased upload limits for pre/post scripts –</strong> Previously, the total size of all pre/post scripts for a deployment was limited to 1 MB. This has now been increased to 1 MB per script, with a total size limit of 4 MB.

#### Fixes

#### Portal

* <strong>Deployments –</strong> Resolved an issue with the Edit button not being displayed if an app has already been successfully deployed.

#### Custom Apps

* Resolved an issue with the MSI Product Code being displayed for a Custom App created with an EXE as the primary installer file.

### 10th July 2024

#### New Features

#### <strong>Portal</strong>

* <strong>Improved sorting by column –</strong> Columns can be sorted by more headings in various nodes when working in the portal.
* <strong>Improved user access requests —</strong> Users can now enter a message giving more information about why they are requesting access to a company.
* <strong>Improved access denied flow  –</strong> Admins can now provide a reason for declining a user's access request.
* <strong>Revoking Access Management rights warning –</strong> Now if you try to revoke Access Management rights for your account, provided at least one other account has this right, you will still be prompted if you are sure you wish to proceed.
* <strong>Search –</strong> General improvements to search.
* <strong>Sync Schedule –</strong> The new [Sync Schedule](https://docs.patchmypc.com/patch-my-pc-cloud/administration/managing-the-sync-schedule) feature allows you to set a different time and frequency for the sync job to run.

#### Fixes

* <strong>Branding –</strong> Resolved an issue where uploading a new logo with the same name as the existing one shows the old logo.
* <strong>Notifications –</strong> Resolved an issue with Teams and Slack notifications cutting off CVE data and not containing release notes.
* <strong>Update reports –</strong> Resolved an issue with the formatting of file sizes on the deployment email report.

### 3rd July 2024

#### New Features

#### Portal

* <strong>Users –</strong> Now you cannot remove the <strong>Access Management</strong> right for the last admin user in your company. This prevents you from locking yourself out of the portal. If you are the last user and there is at least one other account with this right, if you try revoking it from your account, you are prompted to confirm because of the consequences.
* <strong>Users –</strong> The <strong>Application Deployment Admin</strong> user role has been renamed <strong>Intune App Admin</strong>.

#### Intune Apps

* <strong>Naming Conventions -</strong> You can now use the new [Naming Conventions](cloud-administration/manage-cloud-naming-conventions/) feature to configure custom naming conventions for all deployments created in Intune Apps for Cloud. This allows you to standardize the naming convention across all your Intune deployments.

#### Fixes

#### Portal

* <strong>Deployments –</strong> Resolved an issue with two Update-only apps being created in Intune if the first one fails. Now, if an app fails to be created in Intune, we delete it.
* <strong>Onboarding –</strong> Resolved a sign-in issue when a user accepts an invitation.

#### Custom Apps

* Resolved an issue with the <strong>Naming</strong> page not being accessible.

### 26th June 2024

#### New Features

#### Portal

* New [Intune App Admin ](https://docs.patchmypc.com/patch-my-pc-cloud/reference/user-roles)user role added.
* <strong>General –</strong> Clicking our logo in the top left-hand corner of the portal returns you to the App Catalog and forces a refresh.

#### Fixes

#### Portal

* <strong>App Catalog –</strong> If the name of an app is truncated, hovering over it now shows the full name as a tooltip.
* <strong>Contact Form –</strong> Resolved a memory exception error when sending attachments to us through the Contact Form in the portal. You can now send up to 25 MB of attachments when using this form.
* <strong>Deployments –</strong> Resolved issues :
  * with <strong>Pause Updates</strong> being disabled when editing an existing deployment where <strong>Pause Updates</strong> has been enabled.
  * when editing a deployment, any required assignments with an availability date set to <strong>ASAP</strong> are not modified until the next day at 12 AM.
* <strong>Deployment Filters –</strong> When adding a deployment filter to an app deployment, we now only show filters for the <strong>Windows 10 and later</strong> platform, instead of all filters.
* Various improvements to notification messages and tooltips to improve readability.

#### Custom Apps

* Resolved an issue with the user being able to add the same conflicting process multiple times when creating a Custom App. We now do validation to prevent this.

### 19th June 2024

#### New Features

#### Portal

* <strong>Contacting Support –</strong> You can now modify the <strong>From</strong> email address when using the [Contact Support](https://docs.patchmypc.com/patch-my-pc-cloud/contacting-support) form.
* <strong>Environments node –</strong> New [Reconnect ](https://docs.patchmypc.com/patch-my-pc-cloud/administration/managing-your-environments/managing-intune-tenants#reconnecting-an-intune-tenant)button added under the <strong>Intune</strong> connection.
* <strong>Licensing –</strong> If you already have an active license with us and click <strong>Start Trial</strong>, we detect this and use your existing license to activate your portal.
* <strong>Notifications node –</strong> New tooltips have been added so you know when you will receive notifications.
* Primary buttons in the UI re-designed based on user feedback.

#### Fixes

* Various improvements to notification messages and tooltips to improve readability.

### 5th June 2024

#### Fixes

* The “<strong>Prevent from opening an application while the application is updating</strong>” checkbox is no longer checked by default on the <strong>Conflicting Processes</strong> settings pop-up.
* Resolved an issue with the configuration of Conflicting Processes not being honored.
* Various other bugs.