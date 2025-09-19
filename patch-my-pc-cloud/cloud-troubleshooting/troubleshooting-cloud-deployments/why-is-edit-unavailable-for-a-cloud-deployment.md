# Why is “Edit” Unavailable for a Cloud Deployment?

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I am trying to edit a Patch My PC (PMPC) Cloud deployment, but when I view its properties, the **Edit** button is unavailable.

!["Edit" button unavailable on the properties of a deployment](/_images/image-(2047 "\"Edit\" button unavailable on the properties of a deployment").png)

### CAUSE

This is because Update Rings have been configured for this deployment, and when it was created, the [Delayed](../../cloud-deployments/cloud-update-rings/how-cloud-update-rings-are-created.md#delayed-update-rings) option was selected.

### RESOLUTION

As the [Delayed](../../cloud-deployments/cloud-update-rings/how-cloud-update-rings-are-created.md#delayed-update-rings) option was selected for Update Rings when this deployment was created, you cannot edit it until all of the configured Update Rings have finished being created.

> **Note**
>
> See \[Check if an Update Ring has been created]\(../../cloud-deployments/cloud-update-rings/check-if-an-update-ring-has-been-created-in-cloud.md) for more details.