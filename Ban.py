class BanController:
  def __init__(self):
    self.BanList = []

  def GetBanListFromFile(self, path):
    # open file as read
    # test if file opened
    self.BanListFilePath = path
    for line in BanFile:
      self.BanList.append(line)

  def InBanList(self, user):
    if user in self.BanList:
      return True
    else:
      return False

  def Ban(self, user):
    if not self.InBanList(user):
      self.BanList.Append(user)

  def Unban(self, user):
    if self.InBanList(user):
      self.BanList.remove(user)
