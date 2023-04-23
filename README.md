# teststeeleye

In this Project I have made a API Using the Django Rest FrameWork.Also Added the Html5, CSS for thr redirection to the Django brower API Platform.

The main URL for the Project is:-    https://test26600.azurewebsites.net/

<img width="415" alt="image" src="https://user-images.githubusercontent.com/70403163/233835469-44e5d921-7c2c-4fe6-adeb-b0eaa96e4bb3.png">

In this Image we can clearly see that their are Options that are given for the following thimgs to be done:
  1. Search by Using the Trade ID. Just give the select ID in the Box To execute it.
         <img width="959" alt="image" src="https://user-images.githubusercontent.com/70403163/233839378-b8dccdad-130a-4628-b14d-6abae97ebc68.png">
         
         

            
    
  2. By clicking on the View All you Will be Redirected to the Page where all the Data have been shown in the Form of JSON. I have Also Attached the Pagination to it.
          <img width="949" alt="image" src="https://user-images.githubusercontent.com/70403163/233836555-29c2e93e-62dc-40db-8c51-d594956753bf.png">
          
          link:-   https://test26600.azurewebsites.net/trade/
          
          Here the Endpoint to Get all the Data is -----> /trade/
          
          I. Here In the we Can see that We have Pages That is divided into the multiple Pages.
          II. Also we Can see that the whole data has been fetched from the Schema Model.
        
          
  3. The Next Option is the Searching by clicking on this button You will be able to search for the 'counterparty','instrument_id', 'instrument_name', 'trader' That too by giving the starting word Only.
          
        <img width="947" alt="Screenshot 2023-04-23 164805" src="https://user-images.githubusercontent.com/70403163/233837015-e3e9785e-dcf2-4dd6-8aa8-896adac11b4b.png">
          
          link:-   https://test26600.azurewebsites.net/tradesearch/
          
          Here the Endpoint to Search the Data is:- /tradesearch/
          
          examples to Search:- amazon, available, ama , tes , etc 
          
          I. In the Above Exmaple We can see that i have searched for the ama in the search box and as a result i AHve got ther following results.
          
          Note :- In the Staring of the Json Object I have mention that how many The Toatal Number of entries too.
  
  4. The Next Option is of the filtering functionality On clicking on this button we will get directed to the filtering Part of the JSON. The Filtering functionality is given in 'instrument_id', 'asset_class','trade_details__price', 'trade_date_time' .
        
        <img width="945" alt="image" src="https://user-images.githubusercontent.com/70403163/233837323-6b8d1acd-7a07-45a8-b23b-38550be11618.png">
        
           link:-   https://test26600.azurewebsites.net/tradefilter/
           
           Here the Endpoint to Filter the Data on the Basis of Instrument ID:- /tradefilter/?instrument_id=&asset_class=Equity/
          
           I.In the Above Example the Filtering is done between the Aeert Class And the MAX Price and Min Price.

           Note :- In the Staring of the Json Object I have mention that how many The Toatal Number of entries too.


   5. The Last Option is All about the Ordering of the JSON data. In this I have given Ordering of all the atrributes present in the Schema Table so that the Data Present in the Table scan be arranged in the asscem=nding or the descending Order.
   
         <img width="950" alt="image" src="https://user-images.githubusercontent.com/70403163/233838722-96857837-7653-4c23-8937-8cf581fbb880.png">
         
           link:-  https://test26600.azurewebsites.net/tradeordering/
           
           Here the Endpoint to Filter the Data of Trade ID in the Descending order: /tradeordering/?ordering=-id
           
           Here the Endpoint to Filter the Data of Asset Class in the Descending order: /tradeordering/?ordering=asset_class
           
           
           
