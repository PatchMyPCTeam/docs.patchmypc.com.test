# Performing an Application Migration

_Applies to: Patch My PC Cloud_

> **Important**
>
> This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.
>
> Please do not share links to these docs with others outside of the Private Preview.
>
> Once this feature is released, it will be announced and this banner removed.

There are two different types of application migrations we currently support in Patch My PC (PMPC) Cloud, depending on the results of the Migration scan:

* [Migrating a ConfigMgr application to a PMPC App](migrating-a-configmgr-application-to-a-pmpc-app.md)
* [Migrating a ConfigMgr application to a PMPC Custom App](migrating-a-configmgr-application-to-a-pmpc-custom-app.md)

The process to start a migration is the same regardless of the type of target app that will be created in PMPC Cloud/Intune.

To perform a migration:

1. Sign in to your PMPC Cloud Company.
2. Navigate to **Migration**

![Navigating to "Migration"](/_images/image-(14 "Navigating to \"Migration\"").png)

3. Find the application you want to migrate.

![Finding the application to migrate.](/_images/image-(15 "Finding the application to migrate.").png)

> **Tip**
>
> You can use the **Search** box and start typing the name of the application to help you find it.
>
> Alternatively, you can click the filter button and select the checkbox beside the **Match Type** of the application you wish to migrate (**PMPC App** or **Custom App**). Then, click **Apply All Filters** to view only the matching applications.

4. If a warning triangle is not shown in the Info column, go to step 11.

![No warning triangle in the "Info" column](/_images/image-(16 "No warning triangle in the \"Info\" column").png)

5. If a warning triangle is shown in the **Info** column, click it to open the properties of the application.

![Warning triangle shown in the "Info" column](/_images/image-(2715 "Warning triangle shown in the \"Info\" column").png)

6. On the properties of the application, locate the tab(s) with a warning triangle beside them.

![Tabs with a Warning triangle beside them](/_images/image-(2716 "Tabs with a Warning triangle beside them").png)

7. Click the relevant tab and look for the items with the warning triangle beside them.
8. Review the warning and determine your course of action.
9. If you are happy to proceed with the migration, go to step 11.
10. If you cannot proceed with the migration, then close the property of the application and click **Cancel** to close the Migration Wizard. You will now need to determine how you address the warnings to determine your next course of action for this application.
11. Click **Migrate** beside the relevant instance of the app.

![Clicking "Migrate" beside the relevant instance of the app.](/_images/image-(2717 "Clicking \"Migrate\" beside the relevant instance of the app.").png)

12. If the application is being migrated to a PMPC App, follow the [Migrating a ConfigMgr application to a PMPC App](migrating-a-configmgr-application-to-a-pmpc-app.md) process.\\

    If the application is being migrated to a PMPC Custom App, follow the [Migrating a ConfigMgr application to a PMPC Custom App](migrating-a-configmgr-application-to-a-pmpc-custom-app.md) process.