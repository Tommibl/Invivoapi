

class ResponseDataProfile:
    def __init__(self, encryptData, id, userId, phoneNumber, uin, documentNo,
                 firstName, midName, lastName, birthDate, description, sex, type,
                 role, isResident, isSmsSubscribed, isPushSubscribed, isEmailSubscribed,
                 isVirtualUser, created, deviceToken, updated, avatarPath, userLanguage,
                 clinicView, specializationViews, countryCode, email, socialStatusId,
                 subscribeProgram, regionCode):
        self.encryptData = encryptData
        self.id = id
        self.userId = userId
        self.phoneNumber = phoneNumber
        self.uin = uin
        self.documentNo = documentNo
        self.firstName = firstName
        self.midName = midName
        self.lastName = lastName
        self.birthDate = birthDate
        self.description = description
        self.sex = sex
        self.type = type
        self.role = role
        self.isResident = isResident
        self.isSmsSubscribed = isSmsSubscribed
        self.isPushSubscribed = isPushSubscribed
        self.isEmailSubscribed = isEmailSubscribed
        self.isVirtualUser = isVirtualUser
        self.created = created
        self.deviceToken = deviceToken
        self.updated = updated
        self.avatarPath = avatarPath
        self.userLanguage = userLanguage
        self.clinicView = clinicView
        self.specializationViews = specializationViews
        self.countryCode = countryCode
        self.email = email
        self.socialStatusId = socialStatusId
        self.subscribeProgram = subscribeProgram
        self.regionCode = regionCode