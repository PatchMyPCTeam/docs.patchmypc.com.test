# Create Update Rings in Cloud

_Applies to: Patch My PC Cloud_

To create Update Rings for a new Deployment in Patch My PC (PMPC) Cloud:

1. If you are unfamiliar with creating a deployment, follow the [Deploy an App](../deploying-an-app-using-cloud/) process until Step 7.
2.  On the **Assignments** page, click **Enable Update Rings**.\


    ![Clicking “Enable Update Rings](../../../_images/image%20%282110%29.png%20"Clicking%20\"Enable%20Update%20Rings")
3. From the **Update ring start time** dropdown, choose how you want your Update Rings to handle the start times for their assignments:\
   • [Delayed](how-cloud-update-rings-are-created.md#delayed)\
   • [Immediate](how-cloud-update-rings-are-created.md#immediate)

![Choosing the Update Ring start time](../../../_images/image%20%282582%29.png%20"Choosing%20the%20Update%20Ring%20start%20time")

By default, two Update Rings are created with a two-day delay between them.

![Default rings and their settings](../../../_images/image%20%282583%29.png%20"Default%20rings%20and%20their%20settings")

4. If you do not want to add additional Update Rings, go to step 7.\
   \
   To add an additional Update Ring, click **Add Update Ring**.

![Clicking “Add Update Ring”](../../../_images/image%20%282584%29.png%20"Clicking%20\"Add%20Update%20Ring\"")

5. On the **Add Update Ring** dialog box, enter the name for the new ring in the **Name** field and click **Save**.

![“Add Update Ring” dialog box](../../../_images/image%20%282187%29.png%20"\"Add%20Update%20Ring\"%20dialog%20box")

A new ring is added.

![New ring added](../../../_images/image%20%282585%29.png%20"New%20ring%20added")

{% hint style="warning" %}
**Important**

Whenever you add a new Update Ring, it is created with a default delay of **0** days, i.e. the deployment will be installed immediately on any targeted users/devices.

If you already have another ring with a default delay of 0 days, you will see the **Two rings cannot have the same delay value** message besides the second ring with the duplicate delay.

You should adjust the delays on your Update Rings to avoid duplicates.

Also, if your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) is configured for anything other than **Daily**, this will affect the delay you can configure between rings. For example, assuming you have your Sync Schedule configured for **Monthly**, when you add a new ring you will not be able to configure a delay between rings of less than 30 days as shown below.
{% endhint %}

6. Repeat step 4 to add any additional Update Rings.

{% hint style="info" %}
**Note**

You can add up to a maximum of 10 Update Rings per deployment.
{% endhint %}

7. If you do not want to change the names of any of the rings, go to Step 10.\
   \
   If you want to change the name of any of the rings, click the pencil icon (![pencil icon](../../../_images/image%20%282039).png>)) beside the relevant ring.

![Clicking the pencil icon beside the relevant ring to rename](../../../_images/image%20%282591%29.png%20"Clicking%20the%20pencil%20icon%20beside%20the%20relevant%20ring%20to%20rename")

8. Enter the ring's name in the **Name** field of the **Edit Update Ring** dialog box, then click **Save**.

![Entering the ring&#x27;s name in the “Name” field of the “Edit Update Ring” dialog box and clicking “Save”](../../../_images/image%20%282041%29.png%20"Entering%20the%20ring&#x27;s%20name%20in%20the%20\"Name\"%20field%20of%20the%20\"Edit%20Update%20Ring\"%20dialog%20box%20and%20clicking%20\"Save\"")

The updated name appears.

![Updated ring name](../../../_images/image%20%282592%29.png%20"Updated%20ring%20name")

9. Change the name of any other rings.
10. If you do not want to change the delay for any of the rings, go to Step 11.\
    \
    If you want to change the delay for a ring, click the plus (**+**) or minus (**-**) sign beside the relevant rings.

![Clicking plus or minus beside the relevant rings](../../../_images/image%20%282593%29.png%20"Clicking%20plus%20or%20minus%20beside%20the%20relevant%20rings")

11. Click **Add Assignment** and add the relevant assignments for each ring, configuring the settings for each assignment as required.

{% hint style="info" %}
**Note**

See the [Assignments](../deploying-an-app-using-cloud/cloud-assignments-deployment-tab.md) section of the [Deploy an App](../deploying-an-app-using-cloud/) process for more information.
{% endhint %}

{% hint style="success" %}
**Tip**

You can drag assignments between Update Rings by clicking the double ellipsis (<img src="../../../_images/image%20%282044%29.png" alt="double ellipsis" data-size="line">) beside the relevant assignment and dragging and dropping it to the relevant Update Ring.
{% endhint %}

![Assignments added and configured for each Update Ring](../../../_images/image%20%282594%29.png%20"Assignments%20added%20and%20configured%20for%20each%20Update%20Ring")

12. Click **Deploy**.

![Clicking “Deploy”](../../../_images/image%20%282595%29.png%20"Clicking%20\"Deploy\"")

The **“<**_**deployment\_name**_**>” Deployment Summary** dialog box appears, summarizing what you are deploying, to which groups, and when.

![“Deployment Summary”](../../../_images/image%20%282135%29.png%20"\"Deployment%20Summary\"")

{% hint style="info" %}
**Note**

If your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) is set to anything other than **Daily**, the UI will warn you that some rings may not be evaluated as expected.&#x20;

![](../../../_images/image%20%282138).png>)

This is why we recommend you set your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) to **Daily** if you plan to use Update Rings.
{% endhint %}

13. Either click :\
    \
    a. **Cancel** to return to the **Assignments** tab to make any changes (after which you need to click **Deploy**).\
    \
    b. Click **Confirm** to continue.

![Clicking &#x22;Confirm&#x22;](../../../_images/image%20%282140%29.png%20"Clicking%20&#x22;Confirm&#x22;")

When you click **Confirm**, the **Deployments** node appears showing the deployment as **In Progress** and the **Success – Created <**_**deployment\_name**_**>** notification.

![](../../../_images/image%20%282142%29.png%20"")
