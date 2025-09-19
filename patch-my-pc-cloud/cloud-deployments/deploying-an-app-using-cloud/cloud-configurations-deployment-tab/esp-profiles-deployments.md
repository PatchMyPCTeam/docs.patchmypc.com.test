# ESP Profiles (Deployments)

_Applies to: Patch My PC Cloud_

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Using the **ESP Profiles** tool is optional.</p>
</blockquote>

The **ESP Profiles** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to configure your deployments created in our portal to be part of one or more profiles configured on the Enrollment Status Page (ESP) of the Microsoft Intune admin center.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>See <a href="https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enrollment-status">Set up the Enrollment Status Page</a> for more details about the ESP and working with ESP profiles.</p>
</blockquote>

To configure a PMPC Cloud deployment to use an ESP Profile:

1. Ensure the ESP Profile(s) you want this deployment to belong to has already been created in Intune.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>At the time of writing, Intune supports a maximum of 51 profiles plus the default profile (so 52 in total) per tenant.</p>
</blockquote>

2. Click the **ESP Profiles** tool.

![Clicking the “ESP Profiles” tool](/_images/image-(56).png "Clicking the “ESP Profiles” tool")

3. Scroll down to the **ESP Profiles** section.

![Scrolling down to the “ESP Profiles” section](/_images/image-(57).png "Scrolling down to the “ESP Profiles” section")

4. In the **Add Profile** field, either:
   1. Start typing the name of the relevant ESP Profile, then click the checkbox beside it to select it.
   2. Click the dropdown to see a list of existing ESP Profiles and click the&#x20;

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If an ESP Profile already contains the maximum of 100 apps, you will be unable to select it from the dropdown. If you hover over it, you'll see the **Total limit reached** tooltip.</p>
<p>!["Total limit reached" tooltip](/_images/image-(235).png>)&#x20;</p>
</blockquote>

![Selecting the ESP Profile to add this deployment to](/_images/image-(58).png "Selecting the ESP Profile to add this deployment to")

The selected ESP Profile(s) are added to the **Add Profile** field.

![Selected ESP Profiles added to the “Add Profile” field](/_images/image-(59).png "Selected ESP Profiles added to the “Add Profile” field")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can click the **X** beside an ESP Profile in the **Add Profile** field to delete it from the list.</p>
<p>Also, the number in brackets shows the number of apps currently added to an ESP Profile, with 100 being the maximum.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>See [Check ESP Profiles](../../../cloud-reference/intune-reference/check-esp-profiles-in-intune.md) for details on how to check within Intune that a PMPC Cloud deployment has been successfully added to an ESP Profile.</p>
</blockquote>

5. Repeat this process to add any additional ESP Profiles.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>To avoid potential conflicts, we highly recommend you create all of the deployments within the PMPC Cloud portal and use the ESP Profiles feature to control which apps belong to which ESP profiles. You should only use the **Enrollment Status Page** in the Intune admin center to create an ESP Profile.&#x20;</p>
<p>Other important points about ESP Profiles:</p>
<p>* They are currently unavailable on macOS.</p>
<p>* Different ESP Profile can be used in different Update Rings if required.</p>
<p>* If you edit an ESP Profile that is used in a deployment that uses Update Rings, the changes will only be applied to the version of the deployment that is applied to the ring with the lowest delay.</p>
<p>* If during a Sync Schedule the number of apps within an ESP Profile exceeds 100, we do not fail the deployment. The deployment will be completed with any new versions being assigned. However, we will display a warning indicator in the portal and the message \</p>
<p>\</p>
<p>“**Failed to add application with version “<**_**version\_number**_**>” to “<**_**esp\_profile\_name**_**>**”.</p>
</blockquote>

6. If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
   \
   Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

![Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page](/_images/image-(60).png "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page")