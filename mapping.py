import pandas as pd

planets = ['sun','mo','mer','ven','mar','ju','sa','ur','nep','pl']

def init():
    mapping = pd.DataFrame(index=planets,columns=['tick','*','sq','tri','opp'])
    mapping.ix['mo','tick'] = {'sun':245,'mer':145,'ven':146,'mar':147,'ju':148,'sa':149,'ur':150,'ne':151,'pl':254}
    mapping.ix['mo','tri'] = {'sun':246,'mer':152,'ven':153,'mar':154,'ju':155,'sa':156,'ur':157,'ne':158,'pl':255}
    mapping.ix['mo','*'] = {'sun':246,'mer':152,'ven':153,'mar':154,'ju':155,'sa':156,'ur':157,'ne':158,'pl':255}
    mapping.ix['mo','sq'] = {'sun':247,'mer':159,'ven':160,'mar':161,'ju':162,'sa':163,'ur':164,'ne':165,'pl':256}
    mapping.ix['mo','opp'] = {'sun':247,'mer':159,'ven':160,'mar':161,'ju':162,'sa':163,'ur':164,'ne':165,'pl':256}
    mapping.ix['ur','tick'] = {'ne':242,'pl':272}
    mapping.ix['ur','tri'] = {'ne':243,'pl':273}
    mapping.ix['ur','*'] = {'ne':243,'pl':273}
    mapping.ix['ur','sq'] = {'ne':244,'pl':274}
    mapping.ix['ur','opp'] = {'ne':244,'pl':274}
    mapping.ix['ur','tick'] = {'mer':166,'ven':167,'mar':168,'ju':169,'sa':170,'ur':171,'ne':172,'pl':251}
    mapping.ix['sun','tri'] = {'ven':248,'mar':173,'ju':174,'sa':175,'ur':176,'ne':177,'pl':252}
    mapping.ix['sun','*'] = {'ven':248,'mar':173,'ju':174,'sa':175,'ur':176,'ne':177,'pl':252}
    mapping.ix['sun','sq'] = {'mar':178,'ju':179,'sa':180,'ur':181,'ne':182,'pl':253}
    mapping.ix['sun','opp'] = {'mar':178,'ju':179,'sa':180,'ur':181,'ne':182,'pl':253}
    mapping.ix['sa','tick'] = {'ur':236,'ne':237,'pl':269}
    mapping.ix['sa','tri'] = {'ur':238,'ne':239,'pl':270}
    mapping.ix['sa','*'] = {'ur':238,'ne':239,'pl':270}
    mapping.ix['sa','sq'] = {'ur':240,'ne':241,'pl':271}
    mapping.ix['sa','opp'] = {'ur':240,'ne':241,'pl':271}


