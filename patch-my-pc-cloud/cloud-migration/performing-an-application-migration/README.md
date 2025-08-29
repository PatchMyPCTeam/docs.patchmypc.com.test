# Performing an Application Migration

_Applies to: Patch My PC Cloud_

{% hint style="danger" %}
**Important**

This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.

Please do not share links to these docs with others outside of the Private Preview.

Once this feature is released, it will be announced and this banner removed.
{% endhint %}

There are two different types of application migrations we currently support in Patch My PC (PMPC) Cloud, depending on the results of the Migration scan:&#x20;

* [Migrating a ConfigMgr application to a PMPC App](migrating-a-configmgr-application-to-a-pmpc-app.md)&#x20;
* [Migrating a ConfigMgr application to a PMPC Custom App](migrating-a-configmgr-application-to-a-pmpc-custom-app.md)&#x20;

The process to start a migration is the same regardless of the type of target app that will be created in PMPC Cloud/Intune.&#x20;

To perform a migration:&#x20;

1. Sign in to your PMPC Cloud Company.
2. Navigate to **Migration**

<figure><img src="/_images/gitbook/image%20%2814%29.png" alt="Navigating to “Migration”" width="563"><figcaption></figcaption></figure>

3. Find the application you want to migrate.

<figure><img src="/_images/gitbook/image%20%2815%29.png" alt="Finding the application to migrate." width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

You can use the **Search** box and start typing the name of the application to help you find it.

Alternatively, you can click the filter button and select the checkbox beside the **Match Type** of the application you wish to migrate (**PMPC App** or **Custom App**). Then, click **Apply All Filters** to view only the matching applications.
{% endhint %}

4. If a warning triangle is not shown in the Info column, go to step 11.

<figure><img src="/_images/gitbook/image%20%2816%29.png" alt="No warning triangle in the “Info” column" width="563"><figcaption></figcaption></figure>

5. If a warning triangle is shown in the **Info** column, click it to open the properties of the application.

<figure><img src="/_images/gitbook/image%20%282715%29.png" alt="Warning triangle shown in the “Info” column" width="563"><figcaption></figcaption></figure>

6. On the properties of the application, locate the tab(s) with a warning triangle beside them.

<figure><img src="/_images/gitbook/image%20%282716%29.png" alt="Tabs with a Warning triangle beside them" width="563"><figcaption></figcaption></figure>

7. Click the relevant tab and look for the items with the warning triangle beside them.
8. Review the warning and determine your course of action.
9. If you are happy to proceed with the migration, go to step 11.
10. If you cannot proceed with the migration, then close the property of the application and click **Cancel** to close the Migration Wizard. You will now need to determine how you address the warnings to determine your next course of action for this application.
11. Click **Migrate** beside the relevant instance of the app.

<figure><img src="/_images/gitbook/image%20%282717%29.png" alt="Clicking “Migrate” beside the relevant instance of the app." width="563"><figcaption></figcaption></figure>

12. If the application is being migrated to a PMPC App, follow the [Migrating a ConfigMgr application to a PMPC App](migrating-a-configmgr-application-to-a-pmpc-app.md) process.\


    If the application is being migrated to a PMPC Custom App, follow the [Migrating a ConfigMgr application to a PMPC Custom App](migrating-a-configmgr-application-to-a-pmpc-custom-app.md) process.
