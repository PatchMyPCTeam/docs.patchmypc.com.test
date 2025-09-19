# Delete Cloud Branding

_Applies to: Patch My PC Cloud_

{% hint style="danger" %}
**Important**

You cannot delete a Branding App unless it has been deployed successfully or failed to deploy.

Also:

* Each Branding App must contain at least one localization. You cannot delete all localizations for a branding app.
* Deleting a Branding App only removes it from Intune and does not remove any custom logos, files or localizations from your end-user devices. To do this, you need to create an [Uninstall Branding App](uninstall-cloud-branding.md).
{% endhint %}

To delete a Branding App:

1. Navigate to **Settings | Branding**

!\[]\(/\_images/image-(2506 "").png "")

2. Click the ellipsis (`⋮`) button beside the relevant Branding App and select **Delete**.

!\[]\(/\_images/image-(2676 "").png "")

3. Read the **Are you sure** dialog box, and if you want to continue, click **Yes**.

!\[]\(/\_images/image-(2508 "").png "")

The **Success - <**_**branding\_app\_name**_**> deleted** notification is shown.

!\[]\(/\_images/image-(2677 "").png "") deleted notification"" width="563">

The **Branding** screen is redisplayed showing the Branding App has been deleted.

!\[]\(/\_images/image-(2678 "").png "")

{% hint style="success" %}
**Tip**

If you look in the **Events** node, you will see a message stating the Branding App has been deleted.
{% endhint %}
