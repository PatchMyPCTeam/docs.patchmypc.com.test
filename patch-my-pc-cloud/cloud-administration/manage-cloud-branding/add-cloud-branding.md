# Add Cloud Branding

_Applies to: Patch My PC Cloud_

Adding branding to your Patch My PC (PMPC) Cloud company involves:

* [Creating a Branding app](add-cloud-branding.md#creating-a-branding-app)
* [Assigning the Branding app to the relevant audience](add-cloud-branding.md#assigning-the-branding-app-to-the-relevant-audience)
* [Deploying the Branding app](add-cloud-branding.md#deploying-the-branding-app)

### Creating a Branding app

To add a new branding app to your Patch My PC (PMPC) Cloud company:

1. Navigate to <strong>Settings | Branding</strong>

![Navigating to &#x22;Settings | Branding&#x22;](/_images/image-(2422).png "Navigating to &#x22;Settings | Branding&#x22;")

2. Click <strong>Add Branding</strong>

![Clicking &#x22;Add Branding&#x22;](/_images/image-(31).png "Clicking &#x22;Add Branding&#x22;")

3. In the <strong>Branding Intune App Name</strong> field, type a name for the branding app that will be created in Intune, containing your branding. For example, use the <strong>Branding</strong> prefix followed by the name of the Entra ID group this branding app will be deployed to.

![Entering a name of the Branding App](/_images/image-(2492).png "Entering a name of the Branding App")

4. Click <strong>Upload Logo</strong> to upload the logo for your branding that meets the requirements noted on the <strong>Branding</strong> screen.

![Clicking &#x22;Upload Logo&#x22;](/_images/image-(2499).png "Clicking &#x22;Upload Logo&#x22;")

The selected image is shown on the <strong>Branding</strong> screen and the <strong>Notification Preview</strong> updates to show what the notification will look like when shown on the assigned devices.

![Uploaded logo shown on the Branding screen and the &#x22;Notification Preview&#x22; updates to show what the notification will look like when shown on your devices.](/_images/image-(2494).png "Uploaded logo shown on the Branding screen and the &#x22;Notification Preview&#x22; updates to show what the notification will look like when shown on your devices.")

5. Adjust the logo until you are happy.
6. In the <strong>Localizations</strong> section, click the language you want to use to display this branding app on the relevant devices (<strong>English</strong> is selected by default).

![Click the language you want to use in the &#x22;Localizations&#x22; section](/_images/image-(2428).png "Click the language you want to use in the &#x22;Localizations&#x22; section")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Please note the following:</p>
<p>* Changing the localization does not update the <strong>Notification Preview</strong> to that language.</p>
<p>* If a device targeted for this branding app is running a language that is configured under the <strong>Localizations</strong> section, the Manage Conflicting Processes notification will be displayed in the configured language.\</p>
<p>\</p>
<p>However, if the device’s language is different from that set in the branding app, the default language configured in the branding app will be used to display the notification (the default being <strong>English</strong> unless you change it).</p>
<p>* You can only have one localization defined as the default per branding app.</p>
<p>* As ScriptRunner only supports two-letter language codes such as <strong>EN</strong>, <strong>FR</strong>, DE, etc. If the branding app contains a localization for French and the user's device has a system language of <strong>fr-FR</strong>, the user will receive notifications in French. However, if the user's device has the system language <strong>fr-CI</strong> (French in the Ivory Coast), the user will receive notifications in the default language. This is a limitation of ScriptRunner, not PMPC Cloud.</p>
</blockquote>

7. If you need to add a localization for this branding, click <strong>Add Language</strong> and follow the [Add a Localization](manage-localizations-in-cloud.md#add-a-localization) section of [Managing Localizations](manage-localizations-in-cloud.md).

![Clicking &#x22;Add Language&#x22; if you need to add a localization for this branding](/_images/image-(2495).png "Clicking &#x22;Add Language&#x22; if you need to add a localization for this branding")

Now, you need to decide who to assign this branding app to.

### Assigning the Branding app to the relevant audience

To assign a branding app:

1. Click the <strong>Assignments</strong> tab.

![Clicking the &#x22;Assignments&#x22; tab](/_images/image-(2496).png "Clicking the &#x22;Assignments&#x22; tab")

2. Click <strong>Add Assignment</strong>

![Clicking &#x22;Add Assignment&#x22;](/_images/image-(2418).png "Clicking &#x22;Add Assignment&#x22;")

3. On the <strong>Add Required Assignment</strong> screen, choose the relevant users/Entra ID security groups to target for this branding app, then click <strong>Save</strong>.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>Avoid overlapping assignments between Branding Apps. Deploying multiple Branding Apps to the same groups will produce unwanted behavior.</p>
<p>You should also check that if an Uninstall Branding App exists (it will appear at the top of the list of Branding Apps), that the assignments for it don't overlap with those for the new Branding App you are deploying.</p>
</blockquote>

![Choosing the relevant Entra ID security groups to target for this branding app on the &#x22;Add Required Assignment&#x22; screen, then clicking &#x22;Save&#x22;](/_images/image-(2419).png "Choosing the relevant Entra ID security groups to target for this branding app on the &#x22;Add Required Assignment&#x22; screen, then clicking &#x22;Save&#x22;")

The <strong>Assignments</strong> tab is redisplayed, showing all of the assignments for this branding app.

![&#x22;Assignments&#x22; tab showing all of the assignments for this branding app](/_images/image-(2420).png "&#x22;Assignments&#x22; tab showing all of the assignments for this branding app")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>When a branding app is deployed, it overwrites any existing branding app with the same name.</p>
<p>If you deploy multiple branding apps with overlapping assignments, when ScriptRunner executes, it will choose the branding app with the most recent creation/modification date.</p>
<p>For example, branding app A was deployed two months ago, and branding app B was deployed two weeks ago. In this case, branding app B will display the banner.</p>
</blockquote>

### Deploying the Branding app

Once you have configured the branding app and added the required assignments, click <strong>Save</strong> to save and deploy the branding.

![Clicking &#x22;Save&#x22; to save and deploy the branding](/_images/image-(2488).png "Clicking &#x22;Save&#x22; to save and deploy the branding")

The <strong>Success – Branding created</strong> notification is displayed, and the Status of the branding app is shown as <strong>In Progress</strong>.

![&#x22;Success – Branding created&#x22; notification and the &#x22;Status&#x22; of the branding app is shown as &#x22;In Progress&#x22;](/_images/image-(32).png "&#x22;Success – Branding created&#x22; notification and the &#x22;Status&#x22; of the branding app is shown as &#x22;In Progress&#x22;")

Once the branding app has been successfully deployed, the <strong>Status</strong> field will automatically update to <strong>Success</strong> and the <strong>Last update</strong> field will show the last time this branding app was updated.

![&#x22;Status&#x22; field automatically updated to &#x22;Success&#x22; and the &#x22;Last update field&#x22;  showing the last time this branding app was updated.](/_images/image-(33).png "&#x22;Status&#x22; field automatically updated to &#x22;Success&#x22; and the &#x22;Last update field&#x22;  showing the last time this branding app was updated.")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you look in the <strong>Events</strong> section, you see a message stating either:</p>
<p>* <strong>Default Branding <</strong>_<strong>your\_branding\_app\_name</strong>_<strong>> Created -</strong> If you used the default out-the-box logo</p>
<p>* <strong>Custom Branding <</strong>_<strong>your\_branding\_app\_name</strong>_<strong>> Created -</strong> If you upload a custom logo.</p>
</blockquote>

If you look in the Intune admin center, you will see the branding app listed along with your other apps.

![Branding app listed with all of your other apps](/_images/image-(2497).png "Branding app listed with all of your other apps")

When ScriptRunner runs on your devices, it checks to see if the device has the branding. If it doesn't, ScriptRunner installs it.

Also, if a new branding app includes a device that already has branding deployed to it, the branding on the device will be updated to the new branding app.