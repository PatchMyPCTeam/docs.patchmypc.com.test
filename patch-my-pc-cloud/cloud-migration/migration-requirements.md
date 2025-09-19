# Migration Requirements

_Applies to: Patch My PC Cloud_

> **Important**
>
> This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.
>
> Please do not share links to these docs with others outside of the Private Preview.
>
> Once this feature is released, it will be announced and this banner removed.

To use the Migration tool, you need to have a:

* Configuration Manager Primary Site running any version we [officially support](https://patchmypc.com/kb/supported-versions-configuration-manager-wsus/#heading-0).
* Copy of our On-Premises Publisher (Publisher), version 2.1.36.80 or later.
* PMPC Enterprise Premium license if you want:
  * On-Premises Publisher to retrieve a list of applications from your ConfigMgr site and send it to your PMPC Cloud Company.
  * PMPC Cloud to review and evaluate if the application can be migrated to Intune.
  * To be able to click **Migrate** (assuming the app can be migrated), which will allow you to deploy the application to Intune as either a PMPC App or a PMPC Custom App.
* PMPC Enterprise+ license which offers all of the features of Premium, except for last item above (i.e. there is no **Migrate** button to help automate creating the relevant deployment. You will need to manually create the correct deployment type and configure all of the options/settings for the app).
* PMPC Cloud Company:
  * That has been enrolled to the Private Preview and which has the **Migration** feature enabled (if you don’t see the **Migration** node in your portal, then this company hasn’t had this feature enabled).
  * To which you have an account that has been granted the **Full Admin** user role (either by having this account created directly in the Cloud Company or by being a member of an Entra ID Group that has been granted this role).
