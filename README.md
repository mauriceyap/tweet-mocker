pls help i am bored

# Tweet Mocker

AWS Lambda function which listens for tweets from a chosen account, then tweets a SpongeBob Mocking version of it.

## An example

**@SomePretentiousMultinationalCorporation**
Buy our crappy product today because it will improve your life by 164146786%! Join us our customer base today to help 
us make tons of money!

**@You**
bUY OuR crApPY prOdUCt tOdAy BecCAuSe IT wiLL iMproVe yOUR liFe By 164146786%! JOiN OUr cUsToMeR bASe ToDay To hELp Us 
mAke TOns oF MOnEy!

## How to set this up

### Step 1: Set up an AWS Lambda serverless function
*Skip if you know how to do this already. You could also run this on a server - just run `lambda_main.lambda_handler()`*

### Step 2: Make a new Twitter account and get API access

### Step 3: Clone this repo and set up with your access keys

### Step 4: Upload this to Lambda and let it loose
1. Install all the Python dependencies needed for this project. **You'll need to do this on an Ubuntu Linux machine**,
so if you're using Mac or Windows, use a virtual machine or ask an Ubuntu-using friend. From the root of this repo, run:
  - `sudo apt-get install python-pip`
  - `sudo pip install --upgrade pip`
  - `sudo pip install -r requirements.txt -t .`
2. Compress everything in the project folder into a Zip by running:
  - `zip tweet-mocker.zip -r .`
3. Upload it to AWS Lambda
4. Set up the trigger for this function
