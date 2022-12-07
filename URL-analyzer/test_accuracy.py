import os
import requests
from datetime import datetime
import src.algorithmManager as am

def uniquify(path):
    filename = path
    counter = 1

    while os.path.exists(path):
        path = filename + "(" + str(counter) + ")"
        counter += 1

    return path


def test_accuracy(inFileName, outFolder):
    testedURLs = 0
    countPhishingPositives = 0
    lineNum = 0

    outFolderName = uniquify(outFolder)
    print(outFolderName)

    os.mkdir(outFolderName)

    dateFile = open(os.path.join(outFolderName, "Date & Time"), mode='w', encoding='utf-8')
    dateFile.write(datetime.now().strftime('Date: %d/%m/%Y \nTime: %H:%M:%S'))
    dateFile.close()

    wFileWrong = open(os.path.join(outFolderName, "failedURLs").replace("\\", "/"), mode='w', encoding='utf-8')
    wFileWrong.write("These are all of the URLs that the algorithm wrongly classified as not phishingLinks \n\n")
    wFileCorrect = open(os.path.join(outFolderName, "correctURLs").replace("\\", "/"), mode='w', encoding='utf-8')
    wFileCorrect.write("These are all of the URLs that the algorithm correctly classified as phishingLinks \n\n")
    wFileSkipped = open(os.path.join(outFolderName, "skippedURLs").replace("\\", "/"), mode='w', encoding='utf-8')
    wFileSkipped.write("These are all of the URLs that the algorithm skipped due to them being unreachable\n\n")
    wFileRawURLWrong = open(os.path.join(outFolderName, "rawURLFailed").replace("\\", "/"), mode='w', encoding='utf-8')
    wFileRawURLCorrect = open(os.path.join(outFolderName, "rawURLCorrect").replace("\\", "/"), mode='w', encoding='utf-8')

    readFile = open(inFileName, mode='r', encoding='utf-8')

    for line in readFile:
        url = line.strip('\n')
        lineNum += 1
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception("Website does not exist")
        except:
            print(f"Skipping the URL: {url}, beacuse it does not exists.\n")
            wFileSkipped.write(f"{url}\n")
            continue

        print(f"Working on the URL: {url}, on line number: {lineNum}")
        evaluationURL = am.algorithmManager(url)
        var = evaluationURL.run()
        if var:
            wFileRawURLCorrect.write(f"{url}\n")

            countPhishingPositives += 1

            wFileCorrect.write(f"URL: {url} \n")
            wFileCorrect.write(f"Points: {evaluationURL.points} \n\n")
            wFileCorrect.write(f"The website generated the following report:\n")

            for item in evaluationURL.report["URLstringCL"]:
                wFileCorrect.write(f"\t\t{item}\n")
            for item in evaluationURL.report["HTMLdataCL"]:
                wFileCorrect.write(f"\t\t{item}\n")
            for item in evaluationURL.report["DNSdataCL"]:
                wFileCorrect.write(f"\t\t{item}\n")
            for item in evaluationURL.report["DatabaseComparisonCL"]:
                wFileCorrect.write(f"\t\t{item}\n")

            wFileCorrect.write("\n")

            for item in evaluationURL.report["URLreport"][1:]:
                wFileCorrect.write(f"\t{item} \n")

            wFileCorrect.write("\n")

            for item in evaluationURL.report["errors"]:
                wFileCorrect.write(f"{item}\n")

            wFileCorrect.write(f"------------------------\n\n")

        else:
            wFileRawURLWrong.write(f"{url}\n")

            wFileWrong.write(f"URL: {url} \n")
            wFileWrong.write(f"Points: {evaluationURL.points} \n\n")
            wFileWrong.write(f"The website generated the following report:\n")

            for item in evaluationURL.report["URLstringCL"]:
                wFileWrong.write(f"\t\t{item}\n")
            for item in evaluationURL.report["HTMLdataCL"]:
                wFileWrong.write(f"\t\t{item}\n")
            for item in evaluationURL.report["DNSdataCL"]:
                wFileWrong.write(f"\t\t{item}\n")
            for item in evaluationURL.report["DatabaseComparisonCL"]:
                wFileWrong.write(f"\t\t{item}\n")

            wFileWrong.write("\n")

            for item in evaluationURL.report["URLreport"][1:]:
                wFileWrong.write(f"\t{item} \n")

            wFileWrong.write("\n")

            for item in evaluationURL.report["errors"]:
                wFileWrong.write(f"{item}\n")

            wFileWrong.write(f"------------------------\n\n")
        testedURLs += 1

    if (testedURLs == 0): testedURLs = 1

    algorithmAccuracy = round((float(countPhishingPositives)/float(testedURLs))*100)

    print(f"The algorithm accuracy was: {algorithmAccuracy}%")

    # wAccuracyFile = open(os.path.join(outFolderName, f"Algorithm Accuracy: {algorithmAccuracy}%").replace("\\", "/"), mode='w', encoding='utf-8')
    #
    # wAccuracyFile.close()
    readFile.close()
    wFileWrong.close()
    wFileCorrect.close()
    wFileSkipped.close()
    wFileRawURLWrong.close()
    wFileRawURLCorrect.close()


test_accuracy("tests/phishingLinks.txt", "tests/resultFolder")
