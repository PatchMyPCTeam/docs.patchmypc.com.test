# Create Update Rings in Cloud

_Applies to: Patch My PC Cloud_

To create Update Rings for a new Deployment in Patch My PC (PMPC) Cloud:

1. If you are unfamiliar with creating a deployment, follow the [Deploy an App](../deploying-an-app-using-cloud/) process until Step 7.
2.  On the <strong>Assignments</strong> page, click <strong>Enable Update Rings</strong>.\


    ![Clicking “Enable Update Rings](/_images/image-(2110).png "Clicking “Enable Update Rings")
3. From the <strong>Update ring start time</strong> dropdown, choose how you want your Update Rings to handle the start times for their assignments:\
   • [Delayed](how-cloud-update-rings-are-created.md#delayed)\
   • [Immediate](how-cloud-update-rings-are-created.md#immediate)

![Choosing the Update Ring start time](/_images/image-(2582).png "Choosing the Update Ring start time")

By default, two Update Rings are created with a two-day delay between them.

![Default rings and their settings](/_images/image-(2583).png "Default rings and their settings")

4. If you do not want to add additional Update Rings, go to step 7.\
   \
   To add an additional Update Ring, click <strong>Add Update Ring</strong>.

![Clicking “Add Update Ring”](/_images/image-(2584).png "Clicking “Add Update Ring”")

5. On the <strong>Add Update Ring</strong> dialog box, enter the name for the new ring in the <strong>Name</strong> field and click <strong>Save</strong>.

![“Add Update Ring” dialog box](/_images/image-(2187).png "“Add Update Ring” dialog box")

A new ring is added.

![New ring added](/_images/image-(2585).png "New ring added")

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>Whenever you add a new Update Ring, it is created with a default delay of <strong>0</strong> days, i.e. the deployment will be installed immediately on any targeted users/devices.</p>
<p>If you already have another ring with a default delay of 0 days, you will see the <strong>Two rings cannot have the same delay value</strong> message besides the second ring with the duplicate delay.</p>
<p>You should adjust the delays on your Update Rings to avoid duplicates.</p>
<p>Also, if your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) is configured for anything other than <strong>Daily</strong>, this will affect the delay you can configure between rings. For example, assuming you have your Sync Schedule configured for <strong>Monthly</strong>, when you add a new ring you will not be able to configure a delay between rings of less than 30 days as shown below.</p>
</blockquote>

6. Repeat step 4 to add any additional Update Rings.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>You can add up to a maximum of 10 Update Rings per deployment.</p>
</blockquote>

7. If you do not want to change the names of any of the rings, go to Step 10.\
   \
   If you want to change the name of any of the rings, click the pencil icon (![pencil icon](/_images/image-(2039).png>)) beside the relevant ring.

![Clicking the pencil icon beside the relevant ring to rename](/_images/image-(2591).png "Clicking the pencil icon beside the relevant ring to rename")

8. Enter the ring's name in the <strong>Name</strong> field of the <strong>Edit Update Ring</strong> dialog box, then click <strong>Save</strong>.

![Entering the ring&#x27;s name in the “Name” field of the “Edit Update Ring” dialog box and clicking “Save”](/_images/image-(2041).png "Entering the ring&#x27;s name in the “Name” field of the “Edit Update Ring” dialog box and clicking “Save”")

The updated name appears.

![Updated ring name](/_images/image-(2592).png "Updated ring name")

9. Change the name of any other rings.
10. If you do not want to change the delay for any of the rings, go to Step 11.\
    \
    If you want to change the delay for a ring, click the plus (<strong>+</strong>) or minus (<strong>-</strong>) sign beside the relevant rings.

![Clicking plus or minus beside the relevant rings](/_images/image-(2593).png "Clicking plus or minus beside the relevant rings")

11. Click <strong>Add Assignment</strong> and add the relevant assignments for each ring, configuring the settings for each assignment as required.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See the [Assignments](../deploying-an-app-using-cloud/cloud-assignments-deployment-tab.md) section of the [Deploy an App](../deploying-an-app-using-cloud/) process for more information.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can drag assignments between Update Rings by clicking the double ellipsis (![](/_images/image-(2044).png)) beside the relevant assignment and dragging and dropping it to the relevant Update Ring.</p>
</blockquote>

![Assignments added and configured for each Update Ring](/_images/image-(2594).png "Assignments added and configured for each Update Ring")

12. Click <strong>Deploy</strong>.

![Clicking “Deploy”](/_images/image-(2595).png "Clicking “Deploy”")

The <strong>“<</strong>_<strong>deployment\_name</strong>_<strong>>” Deployment Summary</strong> dialog box appears, summarizing what you are deploying, to which groups, and when.

![“Deployment Summary”](/_images/image-(2135).png "“Deployment Summary”")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) is set to anything other than <strong>Daily</strong>, the UI will warn you that some rings may not be evaluated as expected.&#x20;</p>
<p>![](/_images/image-(2138).png>)</p>
<p>This is why we recommend you set your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) to <strong>Daily</strong> if you plan to use Update Rings.</p>
</blockquote>

13. Either click :\
    \
    a. <strong>Cancel</strong> to return to the <strong>Assignments</strong> tab to make any changes (after which you need to click <strong>Deploy</strong>).\
    \
    b. Click <strong>Confirm</strong> to continue.

![Clicking &#x22;Confirm&#x22;](/_images/image-(2140).png "Clicking &#x22;Confirm&#x22;")

When you click <strong>Confirm</strong>, the <strong>Deployments</strong> node appears showing the deployment as <strong>In Progress</strong> and the <strong>Success – Created <</strong>_<strong>deployment\_name</strong>_<strong>></strong> notification.

![](/_images/image-(2142).png "")