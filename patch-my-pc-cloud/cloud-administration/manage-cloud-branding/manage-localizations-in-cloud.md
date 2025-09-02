# Manage Localizations in Cloud

_Applies to: Patch My PC Cloud_

Using the Branding feature of Patch My PC (PMPC) Cloud, you can customize which localizations are used to display the Manage Conflicting Processes notification on your devices.

{% hint style="info" %}
**Note**

The language displayed when the conflicting processes notification appears on devices is determined by the end user's operating system locale:

* If the system locale matches a configured Branding language, the message will be shown in that language.
* If the system locale does not match any configured languages, the message will fall back to the default language set by the Cloud Portal Admin.
{% endhint %}

We recommend you create one branding app per language and then assign this app to the relevant Entra ID Security Groups running the configured language.

Using Branding Apps you can:

* [Add a Localization](manage-localizations-in-cloud.md#add-a-localization)
* [Modify an Localization](manage-localizations-in-cloud.md#modify-an-localization)
* [Delete a Localization](manage-localizations-in-cloud.md#delete-a-localization)

### Add a Localization

To add a Localization:

1. To a new Branding app, follow the [Create a Branding app](add-cloud-branding.md#creating-a-branding-app) process until Step 7.
2. To an existing Branding app, follow the [Modify/Recreate Branding](modify-recreate-cloud-branding.md) process.
3. Click **Add Language**

![Clicking &#x22;Add Language&#x22;](/_images/image-(2405).png "Clicking &#x22;Add Language&#x22;")

4. In the **Language** dropdown of the **Add Localization** screen, start typing the name of the relevant language or select it from the dropdown.

![Typing the name of the relevant language or selecting it from the  &#x22;Language&#x22; dropdown of the &#x22;Add Localization&#x22; screen](/_images/image-(2406).png "Typing the name of the relevant language or selecting it from the  &#x22;Language&#x22; dropdown of the &#x22;Add Localization&#x22; screen")

5. For each of the three tabs (**Install**, **Uninstall**, **Update)**, complete each field with the relevant text and variables you want to use.

![Completing all of the fields on all of the tabs](/_images/image-(2408).png "Completing all of the fields on all of the tabs")

{% hint style="danger" %}
**Important**

When you add a new localization, you must complete all of the fields on all of the tabs before you’ll be able to save it.
{% endhint %}

{% hint style="info" %}
**Tip**

We include common variable names under each field, which you can add by clicking the relevant variable(s).

Also, see [Default Language Notifications](default-language-notifications-in-cloud.md) for a list of the default language notifications for English, which you can use to help you configure other languages.
{% endhint %}

6. Click **Save** to save your settings.

![Clicking &#x22;Save&#x22; to save your settings](/_images/image-(2409).png "Clicking &#x22;Save&#x22; to save your settings")

{% hint style="success" %}
**Tip**

If you make a mistake or want to start again, click **Reset** to reset this screen and start again from the beginning of this process.
{% endhint %}

The **Branding** screen is redisplayed with the newly added localization shown at the top of the list allowing you to select it if required.

![&#x22;Branding&#x22; screen redisplayed with the newly added localization shown at the top of the list allowing you to select it if required](/_images/image-(2410).png "&#x22;Branding&#x22; screen redisplayed with the newly added localization shown at the top of the list allowing you to select it if required")

### Modify an Localization

To modify a Localization for an existing Branding app:

1. Follow the [Edit Branding](modify-recreate-cloud-branding.md#edit-branding) process.
2. Click **Add Language** if you want to add a new language and follow the [Add a Localization](manage-localizations-in-cloud.md#add-a-localization) process.
3. To modify an existing localization, click the pencil icon (![](/_images/image-(2396).png>)) beside the relevant language.

![Clicking the pencil icon beside the relevant language](/_images/image-(2397).png "Clicking the pencil icon beside the relevant language")

4. Make any required changes, then click **Save** to save your changes.

![Clicking &#x22;Save&#x22;](/_images/image-(2398).png "Clicking &#x22;Save&#x22;")

The **Branding** screen is redisplayed.

![&#x22;Branding&#x22; screen is redisplayed](/_images/image-(2399).png "&#x22;Branding&#x22; screen is redisplayed")

5. Click **Save** to save your changes.

![Clicking &#x22;Save&#x22; to save your changes](/_images/image-(2400).png "Clicking &#x22;Save&#x22; to save your changes")

The list of branding apps is displayed along with the **Success – Branding Updated** notification.

![&#x22;Success – Branding Updated&#x22; notification](/_images/image-(2674).png "&#x22;Success – Branding Updated&#x22; notification")

### Delete a Localization

To delete a Localization from either a new or existing branding app:

1. [Edit the branding app](modify-recreate-cloud-branding.md#edit-branding).
2. Click the red trash can beside the language you want to remove.

![Clicking the red trashcan beside the language you want to remove](/_images/image-(2402).png "Clicking the red trashcan beside the language you want to remove")

The language is removed.

3. Click **Save** to save your changes.

![Clicking &#x22;Save&#x22; to save your changes](/_images/image-(2403).png "Clicking &#x22;Save&#x22; to save your changes")

The **Success – Branding updated** notification is displayed.

![&#x22;Success – Branding updated&#x22; notification](/_images/image-(2675).png "&#x22;Success – Branding updated&#x22; notification")