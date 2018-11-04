import json
from anytree import Node, RenderTree

'''

insert query and plan
read plan in json format

process json, read each plan.

'''
# JSON format:
#jsonString = '[{"Plan": {"Node Type": "Hash Join", "Plan": { "Node Type": "Scan"} } }]'


#19 plans in query.json
def getPlans(data):
    plans_count = 0
    isPlanSuccess = False
    isPlansSuccess = False
    hash_table_plans = {}

    for plan_dict in plan_list:
        print("plan_dict keys: ")
        print(plan_dict.keys()) #[u'Execution Time', u'Planning Time', u'Plan', u'Triggers']
        for eachKey in plan_dict:
            if (eachKey == "Plan"):
                isPlanSuccess = True

        # check if there's a key called "Plan"
        if isPlanSuccess == False:
            print("Please insert the correct plan format.")
            break
        
        plan = plan_dict['Plan']
        #print("plan keys: ")
        #print(plan.keys())
        '''u'Temp Written Blocks', u'Node Type', u'Actual Total Time', 
        u'Shared Hit Blocks', u'Inner Unique', u'Plans', ..... '''
        
       
        current_plan = plan
        next_plan = plan
        next_plan_exists = True
        plans_count=plans_count+1
        first_plan = {}

        # process first plan here
        for keyInPlan in current_plan:
            if keyInPlan == "Plans":
                isPlansSuccess = True
            print(str(keyInPlan) + ": " + str(plan[keyInPlan])) # key:value
            #store in hash table of dictionaries
            if keyInPlan != "Plans":
                first_plan[keyInPlan] = str(plan[keyInPlan])

            # do mapping logic for first plan here
            # lineNumberToDisplay = getCorrelation()
        print("first plan:")
        print(first_plan)
        hash_table_plans["1"] = first_plan
        print(hash_table_plans)

        if isPlansSuccess == False:
            print("There is no 'Plans' in this 'Plan'")
            break

        while 'Plans' in next_plan and next_plan_exists:
            next_plan_exists = False
            current_plan = next_plan['Plans']

            # process the other plans here
            for _plan in current_plan:
                plans_count = plans_count + 1
                if 'Plans' in _plan:
                    next_plan_exists = True
                    next_plan = _plan
                
                print("Total Plans: ", plans_count)
                subsequent_plan = {}
                for _keyInPlan in _plan:
                    print(str(_keyInPlan) + ": " + str(_plan[_keyInPlan])) # key:value
                    if _keyInPlan != "Plans":
                        subsequent_plan[_keyInPlan] = str(_plan[_keyInPlan])
                hash_table_plans[str(plans_count)] = subsequent_plan
        print("finally")
        print(hash_table_plans)
        return hash_table_plans
                    # do mapping logic here
                    # lineNumberToDisplay = getCorrelation()



## Main Program ##
with open('query1.json', 'r') as f:
    plan_list = json.load(f)
    
getPlans(plan_list)
