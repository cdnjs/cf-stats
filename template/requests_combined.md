> The first important stat that we are given is the total number of requests sent to cdnjs.cloudflare.com.
> 
> Cloudflare provides this number to us at a 1% sample for the whole month, giving {{REQUESTS_1_PER}} at 1%.\
> This is {{REQUESTS_1_PER_TOTAL}} when multiplied up to 100%.
> 
> We are also given a number of requests for 3 days at a 100% sample, which is {{REQUESTS_3_DAY}}.\
> This is {{REQUESTS_3_DAY_TOTAL}} when recalculated for the {{DAYS}} days of {{MONTH}}.

To provide the best possible estimate for the entire month, an average of both numbers will be used to generate the
 estimate for the final number of requests for the month (75%: 1% month sample data, 25%: 100% 3 day data).\
This results in cdnjs serving approximately {{REQUESTS}} requests in {{MONTH}}.