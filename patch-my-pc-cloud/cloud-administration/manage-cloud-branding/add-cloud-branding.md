# Add Cloud Branding

_Applies to: Patch My PC Cloud_

Adding branding to your Patch My PC (PMPC) Cloud company involves:

* [Creating a Branding app](add-cloud-branding.md#creating-a-branding-app)
* [Assigning the Branding app to the relevant audience](add-cloud-branding.md#assigning-the-branding-app-to-the-relevant-audience)
* [Deploying the Branding app](add-cloud-branding.md#deploying-the-branding-app)

### Creating a Branding app

To add a new branding app to your Patch My PC (PMPC) Cloud company:

1. Navigate to **Settings | Branding**

![Navigating to "Settings | Branding"](/_images/image-(2422Settings-Branding "Navigating to \"Settings | Branding\"").png "Navigating to &#x22;Settings | Branding&#x22;")

2. Click **Add Branding**

![Clicking "Add Branding"](/_images/image-(31Add-Branding "Clicking \"Add Branding\"").png "Clicking &#x22;Add Branding&#x22;")

3. In the **Branding Intune App Name** field, type a name for the branding app that will be created in Intune, containing your branding. For example, use the **Branding** prefix followed by the name of the Entra ID group this branding app will be deployed to.

![Entering a name of the Branding App](/_images/image-(2492 "Entering a name of the Branding App").png "Entering a name of the Branding App")

4. Click **Upload Logo** to upload the logo for your branding that meets the requirements noted on the **Branding** screen.

![Clicking "Upload Logo"](/_images/image-(2499Upload-Logo "Clicking \"Upload Logo\"").png "Clicking &#x22;Upload Logo&#x22;")

The selected image is shown on the **Branding** screen and the **Notification Preview** updates to show what the notification will look like when shown on the assigned devices.

![Uploaded logo shown on the Branding screen and the "Notification Preview" updates to show what the notification will look like when shown on your devices.](/_images/image-(2494Notification-Preview." "Uploaded logo shown on the Branding screen and the \"Notification Preview\" updates to show what the notification will look like when shown on your devices.").png "Uploaded logo shown on the Branding screen and the &#x22;Notification Preview&#x22; updates to show what the notification will look like when shown on your devices.")

5. Adjust the logo until you are happy.
6. In the **Localizations** section, click the language you want to use to display this branding app on the relevant devices (**English** is selected by default).

![Click the language you want to use in the "Localizations" section](/_images/image-(2428Localizations "Click the language you want to use in the \"Localizations\" section").png "Click the language you want to use in the &#x22;Localizations&#x22; section")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Please note the following:</p>
<p>* Changing the localization does not update the **Notification Preview** to that language.</p>
<p>* If a device targeted for this branding app is running a language that is configured under the **Localizations** section, the Manage Conflicting Processes notification will be displayed in the configured language.\</p>
<p>\</p>
<p>However, if the device’s language is different from that set in the branding app, the default language configured in the branding app will be used to display the notification (the default being **English** unless you change it).</p>
<p>* You can only have one localization defined as the default per branding app.</p>
<p>* As ScriptRunner only supports two-letter language codes such as **EN**, **FR**, DE, etc. If the branding app contains a localization for French and the user's device has a system language of **fr-FR**, the user will receive notifications in French. However, if the user's device has the system language **fr-CI** (French in the Ivory Coast), the user will receive notifications in the default language. This is a limitation of ScriptRunner, not PMPC Cloud.</p>
</blockquote>

7. If you need to add a localization for this branding, click **Add Language** and follow the [Add a Localization](manage-localizations-in-cloud.md#add-a-localization) section of [Managing Localizations](manage-localizations-in-cloud.md).

![Clicking "Add Language" if you need to add a localization for this branding](/_images/image-(2495Add-Language "Clicking \"Add Language\" if you need to add a localization for this branding").png "Clicking &#x22;Add Language&#x22; if you need to add a localization for this branding")

Now, you need to decide who to assign this branding app to.

### Assigning the Branding app to the relevant audience

To assign a branding app:

1. Click the **Assignments** tab.

![Clicking the "Assignments" tab](/_images/image-(2496Assignments "Clicking the \"Assignments\" tab").png "Clicking the &#x22;Assignments&#x22; tab")

2. Click **Add Assignment**

![Clicking "Add Assignment"](/_images/image-(2418Add-Assignment "Clicking \"Add Assignment\"").png "Clicking &#x22;Add Assignment&#x22;")

3. On the **Add Required Assignment** screen, choose the relevant users/Entra ID security groups to target for this branding app, then click **Save**.

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>Avoid overlapping assignments between Branding Apps. Deploying multiple Branding Apps to the same groups will produce unwanted behavior.</p>
<p>You should also check that if an Uninstall Branding App exists (it will appear at the top of the list of Branding Apps), that the assignments for it don't overlap with those for the new Branding App you are deploying.</p>
</blockquote>

![Choosing the relevant Entra ID security groups to target for this branding app on the "Add Required Assignment" screen, then clicking "Save"](/_images/image-(2419Add-Required-Assignment "Choosing the relevant Entra ID security groups to target for this branding app on the \"Add Required Assignment\" screen, then clicking \"Save\"").png "Choosing the relevant Entra ID security groups to target for this branding app on the &#x22;Add Required Assignment&#x22; screen, then clicking &#x22;Save&#x22;")

The **Assignments** tab is redisplayed, showing all of the assignments for this branding app.

!["Assignments" tab showing all of the assignments for this branding app](/_images/image-(2420Assignments "\"Assignments\" tab showing all of the assignments for this branding app").png "&#x22;Assignments&#x22; tab showing all of the assignments for this branding app")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>When a branding app is deployed, it overwrites any existing branding app with the same name.</p>
<p>If you deploy multiple branding apps with overlapping assignments, when ScriptRunner executes, it will choose the branding app with the most recent creation/modification date.</p>
<p>For example, branding app A was deployed two months ago, and branding app B was deployed two weeks ago. In this case, branding app B will display the banner.</p>
</blockquote>

### Deploying the Branding app

Once you have configured the branding app and added the required assignments, click **Save** to save and deploy the branding.

![Clicking "Save" to save and deploy the branding](/_images/image-(2488Save "Clicking \"Save\" to save and deploy the branding").png "Clicking &#x22;Save&#x22; to save and deploy the branding")

The **Success – Branding created** notification is displayed, and the Status of the branding app is shown as **In Progress**.

!["Success – Branding created" notification and the "Status" of the branding app is shown as "In Progress"](/_images/image-(32Success-Branding-created "\"Success – Branding created\" notification and the \"Status\" of the branding app is shown as \"In Progress\"").png "&#x22;Success – Branding created&#x22; notification and the &#x22;Status&#x22; of the branding app is shown as &#x22;In Progress&#x22;")

Once the branding app has been successfully deployed, the **Status** field will automatically update to **Success** and the **Last update** field will show the last time this branding app was updated.

!["Status" field automatically updated to "Success" and the "Last update field"  showing the last time this branding app was updated.](/_images/image-(33Status." "\"Status\" field automatically updated to \"Success\" and the \"Last update field\"  showing the last time this branding app was updated.").png "&#x22;Status&#x22; field automatically updated to &#x22;Success&#x22; and the &#x22;Last update field&#x22;  showing the last time this branding app was updated.")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>If you look in the **Events** section, you see a message stating either:</p>
<p>* **Default Branding <**_**your\_branding\_app\_name**_**> Created -** If you used the default out-the-box logo</p>
<p>* **Custom Branding <**_**your\_branding\_app\_name**_**> Created -** If you upload a custom logo.</p>
</blockquote>

If you look in the Intune admin center, you will see the branding app listed along with your other apps.

![Branding app listed with all of your other apps](/_images/image-(2497 "Branding app listed with all of your other apps").png "Branding app listed with all of your other apps")

When ScriptRunner runs on your devices, it checks to see if the device has the branding. If it doesn't, ScriptRunner installs it.

Also, if a new branding app includes a device that already has branding deployed to it, the branding on the device will be updated to the new branding app.