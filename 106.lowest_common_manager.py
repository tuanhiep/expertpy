def getLowestCommonManager(topManager, reportOne, reportTwo):
    # O(n) time | O(d) space - where n is the number of people
    # in the org and d is the depth (height) of the org chart
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager


def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None

    return OrgInfo(lowestCommonManager, numImportantReports)


class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
