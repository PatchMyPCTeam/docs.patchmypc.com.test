# How the Sync Schedule in Cloud affects Update Rings

_Applies to: Patch My PC Cloud_

As the [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) affects when your portal checks for updates to your Patch My PC (PMPC) Cloud deployments, how often it runs can also affect how your Update Rings behave.

For example, if you have deployed an app that updates more frequently than your configured Sync Schedule, the ring with the lowest delay (for example Ring 1) will have the latest suitable version applied.

Depending on how often you run your Sync Schedule and the delay between your rings, the scenario could arise where we have to skip versions to keep everything configured as per your ring strategy.

If this arises, we will not deploy a version of an app to any rings that has not been deployed to at least Ring 1. This ensures we only deploy apps to later rings that have been tested on at least one ring.

### Other Factors

Also:

* If you create your Update Rings with an **Immediate** start time, the Sync Schedule configuration only impacts the daily update of the rings and their assignments (promotion to the new version).
* If you create your Update Rings with the **Delayed** start time, the Sync Schedule configuration impacts both the initial creation of the rings and the daily update of their assignments (promotion to the new version). For example, you create a deployment with two Update Rings with the default two-day delay between them. The first ring will be created when you deploy the software. The second ring won’t be created until two days have passed since the time the deployment was created and the next Sync Schedule run.

The following table summarizes how your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) configuration determines how you can configure the delay between Update Rings.

| Sync Schedule Configured For | Delay between Rings                                                                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Daily                        | Delays between rings can be configured as required.                                                                                                  |
| Weekly                       | <p>Ring 2 has to have a minimum delay of 7 days</p><p>Ring x has to be configured with a delay of at least 7 days apart from any other ring.</p>     |
| Monthly                      | <p>Ring 2 cannot have a delay of less than 31 days</p><p>Ring x has to be configured with a delay of at least 31 days apart from any other ring.</p> |

These limitations ensure that the update delays align with your chosen sync frequency and is why we advise configuring your [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) to run on a daily basis when using Update Rings.