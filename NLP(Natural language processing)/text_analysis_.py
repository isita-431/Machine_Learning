from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def text_analysis(d,n,s):
    words = d.split(' ')
    # print(words[-5:len(words)])
    num = 0
    l=[]
    for i in range(len(words)):
        if words[i]==s:
            num =i
            break
    if num == 0:
        l = words[:n]
    elif num == len(words):
        l = words[-n:len(words)]
    if num != 0 and num-n<0:
        l = words[:num]
    else:
        l = words[num-n:num]
    if num != len(words) and num+n > len(words):
        l.extend(words[num:])
    else:
        l.extend(words[num:num+n])
    s1= ' '.join(l)
    # removing punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    res= tokenizer.tokenize(s1)
    # removing stop words
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(' '.join(res))
    # tokenization
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    return (l,filtered_sentence)



d = """Is telehealth the future of healthcare?Covid-19 has paved the way for advancements in Telehealth services, which have currently become a significant component of the healthcare industry to cope with the social distancing and lockdown measures, people adapted to telehealth services to avail doctor expertise.
Telehealth’s global market size is projected to grow to $55.6 billion by 2025 from $25.4 billion in 2020 at a CAGR of 16.9% during the period.  According to the statistics provided by the Medical Council of India, the doctor-patient ratio currently is 1:2000. Such a low doctor-patient ratio results in most of the population without any access to proper healthcare facilities. The budding digital infrastructure covers the gaps created by the lack of quality hospital infrastructure and medical staff, allowing doctors to converse with patients in the far-flung rural areas, through telemedicine.
Telemedicine will be a major contributor to filling the current gaps in the healthcare industry, a some of the factors contributing to its growth are:
Internet Connectivity:
As internet connectivity in India is currently growing at a rapid pace of 45% as of 2021, this growth will help in further penetrating the market, thus reaching people in areas lacking healthcare facilities. This would avail quality health care services to the people, allowing for efficient and effective treatment of diseases prevalent in the area.
Growing healthcare startups in India
The rapid growth in Digital infrastructure has led to a booming increase in the number of healthcare startups present in India. These start-ups are dedicated to the development of disease tracking and prevention tools. Since most remote areas do not have proper medical facilities or are unable to afford quality healthcare services, these start-ups have developed tools that enable the in-need patients to connect with far-flung doctors to receive affordable medical advice without incurring huge transportation costs. Start-ups such as Practo and 1 MG provide delivery of medicines that are at times not easily available.
Cloud-based and AI telehealth solutions provide tools for employees and companies. These tools help in understanding the onset of diseases, current analysis of the causal factors of prominent diseases, and the most prevalent diseases in the population. Such tools better analyze the causal factors and develop prominent solutions for prevention, thus helping in better disease control for the organization and country.
Companies such as Tata Digital Health provide cloud-based platforms for storing and understanding patient medical records and prescriptions. These help in understanding the track record of the patient, helping doctors to prescribe suitable medicines for the disease.
Self-monitoring and Wearable technology
The growing advancements in technology have enabled the creation of several wearable technologies which would help in better self-tracking of health. The onset of smart-watches and easily available medical devices has resulted in a better collection of medical data. Such devices would help understand the warning signs of certain medical diseases, analyze the trends in their progress and develop better solutions to prevent them.
The increasing cost of medical facilities
With the improvement of medical facilities, the cost of acquiring the facilities is also growing which the majority of the Indian population cannot afford. This issue can be resolved with the advancements of telemedicine which can reduce various expenses like travel for the people which people can utilize in availing better medical practitioners.
Government initiatives
The resolution of the Indian government and various state governments to improve the healthcare facilities and make them accessible to the majority of the people has led them to launch various schemes like Ayushman Bharat which provides free health insurance to the bottom 50% of the population, and Mohalla Clinic, the initiative of Delhi government to provide free medical services for everyone.
    Limitations:
Lack of accuracy: ln doing online consultations the medical practitioners are not able to observe the patient properly they only have to go by what a patient tells them, which reduces the parameters of consideration for them to provide consultations.
Lack of awareness and trust: Most of the population is not aware of these facilities or some of those are not able to trust the technology enough to avail it.
Blackcoffer Insights 40: Rishabh Sarkar and Aayushman Pratap Singh, Jagdish Sheth  School of Management"""
s = "booming"
n= 10
print(text_analysis(d,n,s))
print(text_analysis(d,n,"telehealth"))
