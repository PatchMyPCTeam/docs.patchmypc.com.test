# Cloud "Summary" Deployment tab

_Applies to: Patch My PC Cloud_

> **Note**
>
> Reviewing the **Summary** tab is optional, but recommended.

The **Summary** tab of the Patch My PC (PMPC) Cloud deployment wizard provides a summary of the deployment so you can confirm that it is configured correctly before you create it.

!["Summary" tab](../../../.gitbook/assets/image-\(2391\).png)

Review the summary of the deployment shown on the **Summary** page.\
\
If you are happy click **Deploy**.\
\
If you need to change something, click **< Prev** to backtrack through the Deployment Wizard to the relevant setting. Make the change, then step back through the wizard to this page. If everything is now correct, click **Deploy**.

![Clicking "Deploy"](../../../.gitbook/assets/image-\(2392\).png)

> Note
>
> If you have configured this deployment to use \[Update Rings]\(../cloud-update-rings/), you will see the **Deployment Summary** screen, containing details on how you have configured the rings.
>
> !\["Deployment Summary" shown if this deloyment is using Update Rings]\(/\_images/image-(2291).png>)
>
> See \[Update Rings]\(../cloud-update-rings/) for more information.

The App Catalog is redisplayed along with the **Success - Created&#x20;**_**\<deployment\_name>**_ notification.

![](../../../.gitbook/assets/image-\(2393\).png)

> **Important**
>
> When a new version of software is released, it is automatically deployed using the settings of the existing deployment. The old version will be removed from the target user/device and replaced with the newer version.

> **Note**
>
> By default, the installation logs for an app will be created in the following folder regardless of the installer file type:
>
> \`%ProgramData%\PatchMyPCInstallLogs\`
>
> The only exception is for EXE files, where the specified value for the **loggingSwitch** variable will be used if it is not null or empty.
