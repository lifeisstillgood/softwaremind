#! -*- coding: utf-8 -*-

import docopt
import os

help = """
Will hold list of concepts/chapters and will produce the index.pre and the sep text files

Usage:
  layout.py <indexfile>

Options:
  -h --help Help



"""

chapters = {
        'Software Literacy': '''The idea we should treat software as a new form of *literacy*, 
                                and the implications on a societal scale of everyone being as skilled in 
                                software as they are at reading, writing and arithmetic.''',
        
        'Super Co-operative Species': '''The idea humanity is so successful because we are super- co-opearive,
                                         beyond simply working with family or local tribe, we have discovered 
                                         specialisation, trade and the enormous benefits of being oragnised beyond
                                         our immediate tribal groupings.  ANt colonies are amazing, but where is the inter-colony trade?''',
        
        'Software Mind':     '''We co-operate at enourmous levels, with teams, companies, governments, 
                                nations all forming networks. And these networks carry more than trade or goods - they *learn* - reinforce like tensors. Our organisations are (clay shirkey) Slow AIs.  ''',
        
        'Built Organisations, Deep State': '''Organisations are *built* for certain purposes. The infrastructure forces a certain capability - its hard to make a tank force trasnform to an air force without major capital investment.  But they also have the Slow AI built in - they *think* in certain ways.  Deep State (pace the fake news spin) is where it is hard to change the processes that you do not know about. ''',
        
        'Programmable company': '''SOPPY What if a firms AI, a firms deep state, is encoded and accessible to be read and manipulated. Whether a bank grants a loan to a black family in missiippi can be seen in its code not meerely outcomes.  And what about when it schedules its meetings.  All policy is best expressed as config.''',
        
        'Theory of firm - Coase': '''What determines right size of a firm. What determines who gets to change the encoding of a programmable company. How much deep state can be repalced by re-programming a company.  Who acts int ehc ompany and who acts on the company''',
        
        'The architext Paradox': '''An architect today can <design> a building, but leave many of the detaisl to be worked out at construction time (they of course need to ensure load bearing floors etc etc. But often this not work out - see NEw York famous.) But imagine we create a robot that injects concrete exactly where its told. At this point te architect can churn out hundreds of buildings at a time, but they need to specify *everytrhing*.  This is the problem, opportunity and promise of software as it eats the world - vast savings, vast control, but now everything must be much more explicit.''', 

        'Implicit is now Explicit': '''PArt of architects paradox - enforced openness is the desitnation''',
        
        'The code is the design': '''Articles and discussion - when build is deterministic, the code is the design. SO from now on we see a world of programmable companies which are franchises, with a franchise of one.  Real working policy documents. The goal of SOPpy is to partly allow one to write code that runs a company, but also to write policy documents that read as policy but execute as code. Cucumber ''',
        
        'Enforced Openness': '''We are leading up to the Totalitarian Bet, but its worth noting how VW emissions
        is clear in the codebase.  Its not quite like LIBOR scandal where if there had not been texts explaining "we are going to do a crime" then there simply would have been no proof.  This is where the code base told the Slow AI, the deep state of VW, told the whole org, how to behave. criminally.''',
        
        'MOOP': '''Been banging on about this for a decade. Massive Open Online Psychology. How we behave is visible to all - recordable, analyseable. Is the manager of the team following the 8 leadership principles of google? We expect the maangement to moniotr that. What if the police style body cam strapped to his tiepin just helps that? What happens when the collated experience of 100 million people are condensed into daily advice for a person living their life.
        Not merely sensible index fund investing, but best ways to act with your other half, the advice for working with kids or your manager.  What if instead of taking a pill the best life advice comes from HIPPA level app on your phone.  What if people using this for a decade are measureably fitter, healthier, happier, wealthier than the control group?''',
       
        'Whole Org Test Rig': '''The other important part of the Programmable company - how to find out what changes could have improved your performance over past year.  Replay all the activity against a differetn set of policies / infrastrucutre.  Dont just test will the app survive, test will the org. And will this work best or otehr configurations more effective? ''',
       
       'Totalitarian Bet': '''From guy in guardian. Essence is that China is betting that it can control its citizens using monitoring and social pressure.  Now worth talking about racist assumptions - china has a hugely strong culture of familial devotion and respect built in, so this is not like trying to monitor norweigans or Montana. 
       But it is also a totalitarian regieme using reeducaton camps against racial minority. SO its not nice.
       The problem is two fold. 
       1. This is how society does work.
       2. But its how society decides what is acceptble, what is to be pubished and what not.
       3. this is culture wars.  Is it ok for gay marriage.  My 7yo daughter knows most of the words to Katy Perrys; I kissed a girl (cherry chopsticks!) 

       It will work in reducing open dissent. But will it work in actaually changing minds.

      ''',

      'Democractic Bet':'''That openness leads to better outcomes. Studies on agile in orgs. Military behaviour.
                           Democarcy is waaay newer than we think. And I think tied heavily to scientic method.''',
      
      'coders are the new managers':'''THe new workers are the CPUs. The supervisors and instructions come from the coders - and code is the design.  Look at difference between maangers in Drucker - bestriding the world making decisions, and managers in Googles eight rules - coaches helping keep the employees happy.  And what if employees are not happy - look at OpenAI where an emploee revolt removed the board.  We shall come back to employee ower later. WHy did rome collapse? Collapse of trust and trade.''',
      
      'Non Jobs': '''Non Jobs 80% of 80% -> 96% from 36%. How project manaement will be removed from companies as
      co-ordination is driven through test rigs and APIs and 'measure of progress is workig software' A screed against project maangement-ism.  Also why are companies not using metrics and data to drive outcomes - AB testing your way  to success? Or to be out of a job? ''',
      
       'SDLC as day 2 day':'''Many pieces combine to make modern SDLC - see Joels 12 rules. Policy as code. Software givernance matters - see trolley problems, voting on PRs and VW scandal. End of commerical confidentiality. ''',
      
      'Organisational Mental Health': '''This is similar to, linked to SLow AI and MOOP - how do we create non-dysfunctional organisations? How do we change ourselves and our orgnaisations. How much change to serve the needs of the org is too much? THis is also the essence of the Democratic / Totalitairn bet - balancing the freedom, growth happiness of individuals vs the org whole and the imbalance of wealth and power in the org.  See counselling and divorce rates.  See Post Office scandal in UK - suicides as refusal to admint or understand mistakes. software literacy is accepting bugs as fact of life. ''',
      
      'Equal Say, Equal Share': '''The point is FDR was a traitor to his class.  And that he understood something that is rarely accepted in political circles.  An equal say means an equal share.  And if the answer is 'the plebs only get a say once every four years and the elite get a say every day, look at what explicit implicit and openness directionality means.  There is only so long people can put up with Dark Pools - isnt there? ''',
      
      'Socialist utopia': '''WE live in one. We are dependanet on people we simply dont know. Terry pratchett quote about big lies like truth justice. Other lie is that people will trade without trust. People will self harm without knowing a way back.  Northern Ireland is as good as it gets.  HOw do we build trust in societies and in organisations? ''',
      
      'Rentierism': '''Bad all round. MiltionKeynes. But what does it look like in an organisaiton? Middle management?Finance and 2 order magnitude and equal share and pickeety.  ''',
      
      'Software solves management': '''What is management? A huge part of maangemtn in the change org is co-ordination.  Understanding what is coming down the line and preparing for it. growing a teeth on a cog to meet new teeth.
      But this kind of co-ordiantion problem is much much more soluable with software and programmable companies and whole org tests. By adjusting the policies to come and running models a lot of planned work goes - it simply becomes horse trading.  ''',
      
      'Zipper Project Planning': '''My bugbear. Driving to new york, shouting 'progress reports' back to shore. But similarly people thnking they are such masters of the world they can plan the arrival of new work like a zipper. ''',
      
      '2 Orders of magnitude':'''A way of thinking of responsibility outlines ''',
      
      'Rules vs regulations': '''Regulations are desired states, unable to see down thorugh the 2 orders obscurity.
      Will we simply choose zero crime rates (crime rates are a policy choice)''',
      
      'COmpanies are version numbered': '''Yeah.  ''',
      
      'open source and underfunding of perfect competition': '''Similar to crime rates as policy choice. we want
      capital pooling to exist such that it can be used to provide infrastructutr.  But open source is mostly individual action - if everyone was on UBI would we have better open source? ''',
      

        }


def safename(txt):
    replacetuples = [(' ','_'), (',',''), ('-','')]

    txt = txt.lower()
    for tpl in replacetuples:
        txt = txt.replace(tpl[0], tpl[1])

    return txt

def run(args):
    index = '''
The Software Mind
-----------------

Introduction ... 

'''
    for name, blurb in chapters.items():
        filename = '../docs/newbook/{}.rst'.format(safename(name))
        with open(filename, 'w') as fo:
            fo.write(name + "\n" + "-"*len(name) + "\n\n")
            fo.write(blurb+ '\n\n')
            index += f'<<{filename}>>\n\n'

    with open('../docs/index.pre', 'w') as fo:
        fo.write(index)
    return

    indexfile = args['<indexfile>']
    indexfilename = os.path.basename(os.path.abspath(indexfile))
    rootpath = os.path.dirname(os.path.abspath(indexfile))
    outfile = os.path.join(rootpath, indexfilename.replace(".pre",".rst"))
    outtext = ''
    with open(indexfile, encoding='utf-8') as indexfo:
        for line in indexfo:
            if line.strip().find("{{") == 0: #must be forst thing on a line
                readfrom = line.replace("{","").replace("}","").strip()
                readfrompath = os.path.join(rootpath, readfrom)
                val = gettext(readfrompath)
            else:
                val = line
            outtext += val
    fo = open(outfile, 'w', encoding='utf-8')
    fo.write(outtext)
    fo.close()
    

def main():
    args = docopt.docopt(help)
    run(args)

if __name__ == '__main__':
    main()
