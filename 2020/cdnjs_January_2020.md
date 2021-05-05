# cdnjs January 2020 Usage Stats
Information provided directly by Cloudflare for the `cdnjs.cloudflare.com` domain. ⛅️

A note from the author:

> The folks at Cloudflare have published yet another
> [awesome blog post](https://blog.cloudflare.com/javascript-libraries-are-almost-never-updated/) taking looking at how
> JavaScript libraries on websites are rarely updated once initially added, based on cdnjs usage data and requests.\
> Read the post here: **[JavaScript Libraries Are Almost Never Updated Once Installed](https://blog.cloudflare.com/javascript-libraries-are-almost-never-updated/).**

## Key Highlights
 - This month (January 2020), cdnjs served **over 161 billion requests**. 🖥
 - cdnjs used **a massive consumption of 2.98 PB of data** to serve these requests this month. 📤
 - That works out to **over 96 TB of data and 5.2 billion requests every day** (averaged). 🤯
 - In January, **each request to cdnjs used only 18.51 KB of data on average**. 🔍
 
### Library Highlights
 - **The top library files on cdnjs this month were identical to December, with jQuery (3.3.1/jquery.min.js) taking top
  position once again.**
   - FontAwesome (4.7.0/css/font-awesome.min.css) remained in second with jQuery Mousewheel
   (3.1.13/jquery.mousewheel.min.js) in third.
 - **GSAP remained the top library overall across the top 100 resources, with 13 different versions in the top 100.**
   - The top version requested for GSAP remained 'latest' (not actually the latest version) with 2.2 billion requests,
   followed by version 1.14.2 with 1.8 billion requests. The newly released 3.x versions have yet to make it into the
   cdnjs top 100 resources.
 - **Slick Carousel had a nice bump in requests this month, going from 1.6 billion to 1.8 billion requests.**
   - animate.css also had a jump in total requests for January 2020, with 1.14 billion requests compared to only 1.07
   billion in December. animate.css also had an additional version included in the top 100 for January, version 3.7.2,
   which accounted for 298 million requests (26%).

| Requests & Bandwidth | Top 5 Resources |
|---|---|
| ![cdnjs requests & bandwidth](../cdnjs_total_requests_and_bandwidth.png) | ![cdnjs top 5 resources](../cdnjs_top_5_resources.png) |

## Total Number of Requests
> The first important stat that we are given is the total number of requests sent to cdnjs.cloudflare.com.
> 
> Cloudflare provides this number to us at a 1% sample for the whole month, giving 1,739,515,514 at 1%.\
> This is 173,951,551,400 when multiplied up to 100%.
> 
> We are also given a number of requests for 3 days at a 100% sample, which is 11,933,501,453.\
> This is 123,312,848,348 when recalculated for the 31 days of January.

To provide the best possible estimate for the entire month, an average of both numbers will be used to generate the
 estimate for the final number of requests for the month (75%: 1% month sample data, 25%: 100% 3 day data).\
This results in cdnjs serving approximately 161,291,875,637 requests in January.

**Over 161 billion requests or around 5.2 billion requests each day of January**. 📈

This puts us just shy of the numbers from December, where we saw 5.3 billion requests a day on average, with 165 billion
 overall. This appears to follow the slight downward trend noticed last month, however, our bandwidth usage remains
 almost the same.
 
161 billion requests takes us back to similar traffic levels that we were seeing in August and September of last year
 (164 & 161 billion respectively), before the spike in traffic that was seen in October 2019 (up to 171 billion
 requests).

## Total Bandwidth Usage
> Another great stat that Cloudflare has given us again is the bandwidth usage for the cdnjs.cloudflare.com domain.
> 
> This number, like total requests, is provided at a 1% sample for the month and in gigabytes: 32,185.91 GB.\
> This is 3,218,591.0 GB or 3.22 PB when multiplied up to be 100%.
> 
> Additionally, a 3 day 100% sample is given by Cloudflare at 221,005.71 GB.\
> This results in 2,283,725.7 GB or 2.28 PB for the month.

As with the total number of requests and due to the significant difference between the two, both numbers will be used to
 calculate an average for the final estimate of bandwidth consumed this month (75%: 1% month sample data, 25%: 100% 3
 day data).\
This produces the estimate of 2,984,874.7 GB of bandwidth used for this month by cdnjs.

**This gives cdnjs a massive bandwidth consumption of 2.98 petabytes of data for requests in January**. 🤯

Unlike our requests total for the month, which saw a decrease from last month, the bandwidth consumption for cdnjs in
 January has gone up from 2.92 PB in December to 2.98 PB. This remains very similar to previous months, where we saw
 right around 3 PB in October and November with the slight fall to 2.92 PB in December 2019.

A note from the author regarding totals calculations:

> This month, I decided to change how the totals for requests & bandwidth are calculated across the month. Previously,
> a 50/50 average had been used of the 1% data from the entire month and the 100% 3 day sample given by Cloudflare.
> However, this means that the average generated was heavily based on the data from the last three days and may not been
> very representative of the entire month. To adjust for this, I have changed the weighting used in the calculations so
> that 75% of the average is pulled from the 1% data for the entire month and only 25% is from the 100% 3 day sample. I
> hope this will ensure the approximations generated better reflect the trend of the month whilst also using the 100% 3
> day data to adjust for anything anomalous in the month.

## Top 100 Requested Resources
> These are provided at a 1% sample for the whole of January.
> Bandwidth is measured in gigabytes.
> This data, as well as previous months' data, is available in the SQLite data.db file.

| # | Requests | Bandwidth | cdnjs Resource URL |
|---|----------|-----------|--------------------|
| 1   | 43,662,961 | 1,184.52 | [cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js)                                                             |
| 2   | 43,134,279 |   285.25 | [cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css)                           |
| 3   | 32,878,820 |    58.26 | [cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.13/jquery.mousewheel.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.13/jquery.mousewheel.min.js)               |
| 4   | 32,348,395 | 2,267.00 | [cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/fonts/fontawesome-webfont.woff2](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/fonts/fontawesome-webfont.woff2)             |
| 5   | 22,962,600 |   758.08 | [cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenMax.min.js)                                                           |
| 6   | 18,334,921 | 1,739.86 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.14.2/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.14.2/TweenMax.min.js)                                                           |
| 7   | 16,757,853 |   476.54 | [cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js)                                                             |
| 8   | 16,559,690 |   107.26 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.js](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.js)                               |
| 9   | 16,289,579 |    26.43 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.css](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.css)                             |
| 10  | 13,913,895 |    17.56 | [cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js)                                 |
| 11  | 13,061,185 |   406.99 | [cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js)                                                           |
| 12  | 10,774,600 |    69.74 | [cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js)                                             |
| 13  | 9,582,241  |    17.17 | [cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.12/jquery.mousewheel.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.12/jquery.mousewheel.min.js)               |
| 14  | 9,438,277  |   337.04 | [cdnjs.cloudflare.com/ajax/libs/gsap/2.0.2/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.2/TweenMax.min.js)                                                             |
| 15  | 9,015,962  |   251.51 | [cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js)                                                             |
| 16  | 8,637,272  |    14.20 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css)                             |
| 17  | 8,624,713  |    58.08 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js)                               |
| 18  | 8,340,623  |    38.59 | [cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js](https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js)                                                 |
| 19  | 7,363,777  |   253.66 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.19.0/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.19.0/TweenMax.min.js)                                                           |
| 20  | 6,956,592  |    44.96 | [cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js)                                             |
| 21  | 6,820,986  |    48.06 | [cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js)                                             |
| 22  | 6,799,953  |   251.87 | [cdnjs.cloudflare.com/ajax/libs/gsap/2.1.3/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.3/TweenMax.min.js)                                                             |
| 23  | 6,704,959  |   185.27 | [cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js)                                                             |
| 24  | 6,673,904  |    15.34 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/cookieconsent.min.js](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/cookieconsent.min.js)                               |
| 25  | 6,652,376  |    79.01 | [cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.core.min.js](https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.core.min.js)                                         |
| 26  | 6,410,754  |    38.04 | [cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js](https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js)                                       |
| 27  | 6,300,821  |   221.50 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.20.2/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.20.2/TweenMax.min.js)                                                           |
| 28  | 6,269,662  |    24.76 | [cdnjs.cloudflare.com/ajax/libs/json3/3.3.2/json3.min.js](https://cdnjs.cloudflare.com/ajax/libs/json3/3.3.2/json3.min.js)                                                                 |
| 29  | 6,086,685  |    35.20 | [cdnjs.cloudflare.com/ajax/libs/postscribe/2.0.8/postscribe.min.js](https://cdnjs.cloudflare.com/ajax/libs/postscribe/2.0.8/postscribe.min.js)                                             |
| 30  | 6,083,368  |   163.29 | [cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js)                                                             |
| 31  | 6,014,750  |   206.36 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.19.1/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.19.1/TweenMax.min.js)                                                           |
| 32  | 5,992,327  |    58.78 | [cdnjs.cloudflare.com/ajax/libs/lodash.js/2.4.1/lodash.mobile.min.js](https://cdnjs.cloudflare.com/ajax/libs/lodash.js/2.4.1/lodash.mobile.min.js)                                         |
| 33  | 5,987,861  |    41.11 | [cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js)                                             |
| 34  | 5,653,461  |    24.61 | [cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css](https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css)                                               |
| 35  | 5,408,243  |   147.42 | [cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js)                                                             |
| 36  | 5,304,199  |    37.29 | [cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css)                                   |
| 37  | 5,284,033  |   185.81 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.20.3/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.20.3/TweenMax.min.js)                                                           |
| 38  | 5,195,115  |     5.66 | [cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.css](https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.css)                                             |
| 39  | 5,174,660  |    77.81 | [cdnjs.cloudflare.com/ajax/libs/mobile-detect/1.4.3/mobile-detect.min.js](https://cdnjs.cloudflare.com/ajax/libs/mobile-detect/1.4.3/mobile-detect.min.js)                                 |
| 40  | 5,084,271  |   185.63 | [cdnjs.cloudflare.com/ajax/libs/gsap/2.1.2/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.2/TweenMax.min.js)                                                             |
| 41  | 4,996,218  |   163.74 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.18.0/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.18.0/TweenMax.min.js)                                                           |
| 42  | 4,982,903  |   379.67 | [cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js](https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js)                                                 |
| 43  | 4,978,635  |    72.03 | [cdnjs.cloudflare.com/ajax/libs/gsap/latest/plugins/CSSPlugin.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/plugins/CSSPlugin.min.js)                                         |
| 44  | 4,971,057  |    15.83 | [cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js](https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js)                                           |
| 45  | 4,968,573  |   138.17 | [cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js)                                                             |
| 46  | 4,509,474  |    11.11 | [cdnjs.cloudflare.com/ajax/libs/gsap/latest/easing/EasePack.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/easing/EasePack.min.js)                                             |
| 47  | 4,412,642  |    14.69 | [cdnjs.cloudflare.com/ajax/libs/Swiper/4.5.0/css/swiper.min.css](https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.5.0/css/swiper.min.css)                                                   |
| 48  | 4,369,810  |    40.73 | [cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js](https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js)                           |
| 49  | 4,262,410  |    23.48 | [cdnjs.cloudflare.com/ajax/libs/bxslider/4.1.2/jquery.bxslider.min.js](https://cdnjs.cloudflare.com/ajax/libs/bxslider/4.1.2/jquery.bxslider.min.js)                                       |
| 50  | 4,233,442  |     7.72 | [cdnjs.cloudflare.com/ajax/libs/jquery.lazyload/1.9.1/jquery.lazyload.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery.lazyload/1.9.1/jquery.lazyload.min.js)                         |
| 51  | 4,176,519  |    44.11 | [cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.js](https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.js)                                               |
| 52  | 4,172,832  |    39.06 | [cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenLite.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenLite.min.js)                                                         |
| 53  | 4,125,808  |    25.91 | [cdnjs.cloudflare.com/ajax/libs/bxslider/4.2.12/jquery.bxslider.min.js](https://cdnjs.cloudflare.com/ajax/libs/bxslider/4.2.12/jquery.bxslider.min.js)                                     |
| 54  | 4,098,782  |    22.13 | [cdnjs.cloudflare.com/ajax/libs/iframe-resizer/3.5.15/iframeResizer.contentWindow.min.js](https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/3.5.15/iframeResizer.contentWindow.min.js) |
| 55  | 4,037,294  |   121.22 | [cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js)                                                             |
| 56  | 4,012,523  |    69.98 | [cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css](https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css)                       |
| 57  | 3,945,594  |    23.51 | [cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css)                           |
| 58  | 3,906,177  |    61.89 | [cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js](https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js)                                                     |
| 59  | 3,850,333  |   135.57 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.20.4/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.20.4/TweenMax.min.js)                                                           |
| 60  | 3,841,155  |   116.57 | [cdnjs.cloudflare.com/ajax/libs/Swiper/4.5.0/js/swiper.min.js](https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.5.0/js/swiper.min.js)                                                       |
| 61  | 3,838,331  |     2.20 | [cdnjs.cloudflare.com/ajax/libs/tinymce/3.5.8/plugins/example/langs/en.min.js](https://cdnjs.cloudflare.com/ajax/libs/tinymce/3.5.8/plugins/example/langs/en.min.js)                       |
| 62  | 3,594,518  |   128.46 | [cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenMax.min.js)                                                             |
| 63  | 3,550,113  |     8.09 | [cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js)                                     |
| 64  | 3,466,067  |     4.99 | [cdnjs.cloudflare.com/ajax/libs/js-cookie/2.2.0/js.cookie.min.js](https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.2.0/js.cookie.min.js)                                                 |
| 65  | 3,458,821  |    12.15 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/logo.png](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/logo.png)                                                       |
| 66  | 3,390,376  |     7.96 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.10/cookieconsent.min.js](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.10/cookieconsent.min.js)                             |
| 67  | 3,373,151  |     6.99 | [cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js](https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js)                                         |
| 68  | 3,356,589  |   104.01 | [cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.min.js)                                                           |
| 69  | 3,343,622  |     4.61 | [cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css](https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css)                                               |
| 70  | 3,332,022  |    13.94 | [cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.1/jquery-migrate.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.1/jquery-migrate.min.js)                             |
| 71  | 3,317,667  |     6.69 | [cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/magnific-popup.min.css](https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/magnific-popup.min.css)                     |
| 72  | 3,293,282  |    89.53 | [cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.7/js/swiper.min.js](https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.7/js/swiper.min.js)                                                       |
| 73  | 3,267,066  |     3.57 | [cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.css](https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.css)                                             |
| 74  | 3,224,941  |    23.45 | [cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js](https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js)                           |
| 75  | 3,202,700  |    10.41 | [cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.7/css/swiper.min.css](https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.7/css/swiper.min.css)                                                   |
| 76  | 3,201,718  |    36.67 | [cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js](https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js)                                     |
| 77  | 3,165,324  |   105.73 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.18.2/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.18.2/TweenMax.min.js)                                                           |
| 78  | 3,109,326  |     4.92 | [cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css](https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css)                     |
| 79  | 3,093,089  |   162.68 | [cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/fonts/fontawesome-webfont.woff2](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/fonts/fontawesome-webfont.woff2)             |
| 80  | 3,086,012  |     3.69 | [cdnjs.cloudflare.com/ajax/libs/jqueryui-touch-punch/0.2.3/jquery.ui.touch-punch.min.js](https://cdnjs.cloudflare.com/ajax/libs/jqueryui-touch-punch/0.2.3/jquery.ui.touch-punch.min.js)   |
| 81  | 3,059,792  |    16.07 | [cdnjs.cloudflare.com/ajax/libs/react/16.8.6/umd/react.production.min.js](https://cdnjs.cloudflare.com/ajax/libs/react/16.8.6/umd/react.production.min.js)                                 |
| 82  | 3,044,745  |   213.83 | [cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.woff2](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/webfonts/fa-solid-900.woff2)                   |
| 83  | 3,034,385  |    22.84 | [cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/jquery.magnific-popup.min.js](https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/jquery.magnific-popup.min.js)         |
| 84  | 3,026,590  |    93.47 | [cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js)                                                             |
| 85  | 3,024,249  |    95.80 | [cdnjs.cloudflare.com/ajax/libs/react-dom/16.8.6/umd/react-dom.production.min.js](https://cdnjs.cloudflare.com/ajax/libs/react-dom/16.8.6/umd/react-dom.production.min.js)                 |
| 86  | 3,011,214  |     4.00 | [cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick-theme.min.css](https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick-theme.min.css)                                 |
| 87  | 3,006,775  |    83.64 | [cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js)                                                             |
| 88  | 2,985,822  |     9.32 | [cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css](https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css)                                               |
| 89  | 2,926,986  |    21.52 | [cdnjs.cloudflare.com/ajax/libs/dexie/2.0.4/dexie.min.js](https://cdnjs.cloudflare.com/ajax/libs/dexie/2.0.4/dexie.min.js)                                                                 |
| 90  | 2,921,441  |    92.01 | [cdnjs.cloudflare.com/ajax/libs/babel-polyfill/6.26.0/polyfill.min.js](https://cdnjs.cloudflare.com/ajax/libs/babel-polyfill/6.26.0/polyfill.min.js)                                       |
| 91  | 2,912,647  |    41.97 | [cdnjs.cloudflare.com/ajax/libs/gsap/1.18.0/plugins/CSSPlugin.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/1.18.0/plugins/CSSPlugin.min.js)                                         |
| 92  | 2,908,263  |    24.49 | [cdnjs.cloudflare.com/ajax/libs/iScroll/5.2.0/iscroll.min.js](https://cdnjs.cloudflare.com/ajax/libs/iScroll/5.2.0/iscroll.min.js)                                                         |
| 93  | 2,866,921  |     3.91 | [cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/dark-bottom.css](https://cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/dark-bottom.css)                                         |
| 94  | 2,865,190  |    86.25 | [cdnjs.cloudflare.com/ajax/libs/babel-polyfill/6.23.0/polyfill.min.js](https://cdnjs.cloudflare.com/ajax/libs/babel-polyfill/6.23.0/polyfill.min.js)                                       |
| 95  | 2,813,074  |    12.53 | [cdnjs.cloudflare.com/ajax/libs/gsap/latest/TimelineLite.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/TimelineLite.min.js)                                                   |
| 96  | 2,794,527  |    50.29 | [cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js](https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js)                                                                 |
| 97  | 2,776,324  |    86.49 | [cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js)                                                           |
| 98  | 2,755,388  |    84.38 | [cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.js](https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.js)                                                     |
| 99  | 2,754,293  |    12.95 | [cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css](https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css)                                               |
| 100 | 2,745,406  |    27.95 | [cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.js](https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.js)                                               |

Author: [Matt (IPv4) Cowley](https://mattcowley.co.uk) - If there are any errors, please let me know and I will
 endeavour to correct them.
