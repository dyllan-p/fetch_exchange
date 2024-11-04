#include <stdio.h>
#include <curl/curl.h>

#define API_KEY ""
#define BASE "USD"
#define SYMBOLS "ZAR"

int main(void) {
	const char* url = "http://data.fixer.io/api/latest?access_key="
					 API_KEY
					 "&base="
					 BASE
					 "&symbols="
					 SYMBOLS;

	CURL *curl;
	CURLcode res;

	curl_global_init(CURL_GLOBAL_DEFAULT);

	curl = curl_easy_init();
	if(curl) {
		curl_easy_setopt(curl, CURLOPT_URL, url);
		res = curl_easy_perform(curl);
		if(res != CURLE_OK) {
		    fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
		}
		curl_easy_cleanup(curl);
	}
	
	curl_global_cleanup();
	   
	return 0;
}

