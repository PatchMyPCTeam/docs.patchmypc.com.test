# Performing an Application Migration

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.</p>
<p>Please do not share links to these docs with others outside of the Private Preview.</p>
<p>Once this feature is released, it will be announced and this banner removed.</p>
</blockquote>

There are two different types of application migrations we currently support in Patch My PC (PMPC) Cloud, depending on the results of the Migration scan:&#x20;

* [Migrating a ConfigMgr application to a PMPC App](migrating-a-configmgr-application-to-a-pmpc-app.md)&#x20;
* [Migrating a ConfigMgr application to a PMPC Custom App](migrating-a-configmgr-application-to-a-pmpc-custom-app.md)&#x20;

The process to start a migration is the same regardless of the type of target app that will be created in PMPC Cloud/Intune.&#x20;

To perform a migration:&#x20;

1. Sign in to your PMPC Cloud Company.
2. Navigate to **Migration**

![Navigating to "Migration"](/_images/image-(14).png "Navigating to “Migration”")

3. Find the application you want to migrate.

![Finding the application to migrate.](/_images/image-(15).png "Finding the application to migrate.")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can use the **Search** box and start typing the name of the application to help you find it.</p>
<p>Alternatively, you can click the filter button and select the checkbox beside the **Match Type** of the application you wish to migrate (**PMPC App** or **Custom App**). Then, click **Apply All Filters** to view only the matching applications.</p>
</blockquote>

4. If a warning triangle is not shown in the Info column, go to step 11.

![No warning triangle in the "Info" column](/_images/image-(16).png "No warning triangle in the “Info” column")

5. If a warning triangle is shown in the **Info** column, click it to open the properties of the application.

![Warning triangle shown in the "Info" column](/_images/image-(2715).png "Warning triangle shown in the “Info” column")

6. On the properties of the application, locate the tab(s) with a warning triangle beside them.

![Tabs with a Warning triangle beside them](/_images/image-(2716).png "Tabs with a Warning triangle beside them")

7. Click the relevant tab and look for the items with the warning triangle beside them.
8. Review the warning and determine your course of action.
9. If you are happy to proceed with the migration, go to step 11.
10. If you cannot proceed with the migration, then close the property of the application and click **Cancel** to close the Migration Wizard. You will now need to determine how you address the warnings to determine your next course of action for this application.
11. Click **Migrate** beside the relevant instance of the app.

![Clicking "Migrate" beside the relevant instance of the app.](/_images/image-(2717).png "Clicking “Migrate” beside the relevant instance of the app.")

12. If the application is being migrated to a PMPC App, follow the [Migrating a ConfigMgr application to a PMPC App](migrating-a-configmgr-application-to-a-pmpc-app.md) process.\


    If the application is being migrated to a PMPC Custom App, follow the [Migrating a ConfigMgr application to a PMPC Custom App](migrating-a-configmgr-application-to-a-pmpc-custom-app.md) process.