# Manage Cloud Branding

_Applies to: Patch My PC Cloud_

Intune Apps for Patch My PC (PMPC) Cloud allows you to configure your company's branding, which is shown to users whenever software is installed or updated using Manage Conflicting Processes notifications.

Adding branding packages the settings for Manage Conflicting Processes into its own app, which is managed by Intune Apps. This application is published to Intune, where it’s deployed to the following location on all of your devices:

```
C:\ProgramData\PatchMyPC\Notification\
```

All branding-related tasks are performed from the <strong>Branding</strong> node of the portal, which is accessed by:

1. Sign in to the PMPC Portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2.  Navigate to <strong>Settings | Branding</strong>.\


    ![Navigating to “Settings | Branding”](/_images/image-(1477).png "Navigating to “Settings | Branding”")

The <strong>Branding</strong> screen is then displayed, allowing you to:

* [Add Branding](add-cloud-branding.md)
* [Modify/Recreate Branding](modify-recreate-cloud-branding.md)
* [Manage Localizations](manage-localizations-in-cloud.md)
* [Delete Branding](delete-cloud-branding.md)
* [Uninstall Branding](uninstall-cloud-branding.md)

![“Branding” screen](/_images/image-(1478).png "“Branding” screen")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you do not add branding, our default branding shown on the <strong>Branding</strong> page will be used for all Intune App-related notifications on your computers.</p>
<p>![Default Intune Apps for Cloud branding](/_images/image-(1479).png>)</p>
</blockquote>