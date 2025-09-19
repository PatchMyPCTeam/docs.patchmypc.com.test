# Delete Update Rings in Cloud

_Applies to: Patch My PC Cloud_

For a Patch My PC (PMPC) Cloud deployment with Update Rings enabled, you can either:

* [Delete all Update Rings](delete-update-rings-in-cloud.md#delete-all-update-rings)
* [Delete a Single Update Ring](delete-update-rings-in-cloud.md#delete-a-single-update-ring)

{% hint style="info" %}
**Note**

All deletion tasks for Update Rings are performed from the **Assignments** tab of the respective deployment.
{% endhint %}

### Delete all Update Rings

To delete all Update Rings for a deployment:

1. [Edit](../manage-cloud-deployments/edit-a-cloud-deployment.md) the relevant deployment and navigate to the **Assignments** tab.
2.  If you want to delete a single Update Ring, use the [Delete a Single Update Ring](delete-update-rings-in-cloud.md#delete-a-single-update-ring) process.\
    \
    To delete all Update Rings for this deployment, click **Remove all Rings**.\\

    !\[]\(/\_images/image-(2061 "").png "")
3.  On the **Move Assignments or Delete** dialog box, click **Move** to remove the Update Rings but keep all the existing assignments.\
    \\

    !\[]\(/\_images/image-(2062 "").png "")

{% hint style="info" %}
**Note**

Clicking **Delete** will delete any existing assignments but not the deployment itself.

![Clicking “Delete” will delete any existing assignments, not the deployment itself.](<../../../.gitbook/assets/image (2064).png>)\\
{% endhint %}

The Update Rings are removed and any existing assignments are kept.

!\[]\(/\_images/image-(2065 "").png "")

4.  Click **Save** to save your changes.\
    \\

    !\[]\(/\_images/image-(2066 "").png "")

{% hint style="warning" %}
**Important**

As removing all Update Rings disables Update Ring functionality for this deployment (which could result in unintended results), the **"**_**\<deployment\_name>**_**" Deployment Summary** is shown detailing the impact of your proposed change.\
\
For example, this version of the app will be deployed immediately to all of the following assignments without any of the delays enforced by using Update Rings.

<img src="../../../.gitbook/assets/image (2067).png" alt="“Deployment Summary” showing the impact of deleting all Update Rings" data-size="original">
{% endhint %}

{% hint style="info" %}
**Note**

If the existing deployment had different versions applied to different assignments, we use the version that was applied to the lowest delay ring before the deployment was edited.
{% endhint %}

5.  Click **Cancel** to return to the **Assignments** tab to make any required changes, or click **Confirm** to save your changes.\
    \
    The **Deployments** node is displayed along with the **Success – Edited <**_**deployment\_name**_**>** notification.\
    \\

    !\[]\(/\_images/image-(2068 "").png "")

{% hint style="success" %}
**Tip**

If you edit the deployment and click **More Info**, you will see the tabs representing the Update Rings are no longer present.
{% endhint %}

### Delete a Single Update Ring

To delete a Single Update Ring:

1. Navigate to the **Assignments** page of the deployment.
2. Click the red **X** beside the Update Ring you want to delete.

{% hint style="info" %}
**Note**

Deleting an Update Ring also deletes any assignments controlled by that ring. If you want to keep the assignment, drag and drop it to another ring before you delete the ring.
{% endhint %}

!\[]\(/\_images/image-(2069 "").png "")

The ring and any assignments it contains are deleted.

!\[]\(/\_images/image-(2070 "").png "")

3.  Click **Save** to save your changes.\
    \\

    !\[]\(/\_images/image-(2071 "").png "")

    \
    As you’ve removed an Update Ring and it’s assignments, the **"<**_**deployment\_name**_**>" Deployment Summary** is shown detailing the impact of your proposed change.\
    \
    For example, by deleting the **7-Zip Pilot +7 Days** ring, this app will not be deployed to the **03 - Patching - Production - All - 7 Days** Entra ID group.\
    \\

    !\[]\(/\_images/image-(2072 "").png "")
4.  Click **Cancel** to return to the **Assignments** tab to make any required changes, or click **Confirm** to save your changes.\
    \
    The **Deployments** node is displayed along with the **Success – Edited <**_**deployment\_name**_**>** notification.\\

    !\[]\(/\_images/image-(2073 "").png "")

{% hint style="success" %}
**Tip**

If you edit the deployment and click **More Info**, you will see the tab representing the deleted Update Ring is no longer present.
{% endhint %}
